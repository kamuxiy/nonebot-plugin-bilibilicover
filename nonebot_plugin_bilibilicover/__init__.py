from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import urllib3
import json

bphoto = on_command("/封面图", priority=5)


@bphoto.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数
    if args:
        state["AV"] = args  # 如果用户发送了参数则直接赋值


@bphoto.got("AV", prompt="你想查询哪个视频的封面图呢？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    AV = state["AV"]
    if AV[0:2] not in ["av", "BV"]:
        await bphoto.reject("你想查询的AV或BV号无法查询，请重新输入！")
    else:
        await bphoto.finish("取消查询")
    bcover = await get_bcover(AV)
    await bphoto.finish(bcover)


async def get_bcover(AV: str):
    try:
        if AV[0:2] in ["BV"]:
            table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
            tr = {}
            for i in range(58):
                tr[table[i]] = i
            s = [11, 10, 3, 8, 4, 6]
            xor = 177451812
            add = 8728348608

            async def dec(x):
                r = 0
                for i in range(6):
                    r += tr[x[s[i]]] * 58 ** i
                return "av" + str((r - add) ^ xor)

            BV = await dec(AV)
            url = 'https://www.kamuxiy.top/demo/bilibiliapi/?AV_number=' + BV
            r = urllib3.PoolManager().request('GET', url)
            hjson = json.loads(r.data.decode())
            img_url = hjson['img_url']
            cq = "[CQ:image,file=" + img_url + ",id=40000]"
            return f"{AV}的封面图是...\n" + Message(cq)

        else:
            url = 'https://www.kamuxiy.top/demo/bilibiliapi/?AV_number=' + AV
            r = urllib3.PoolManager().request('GET', url)
            hjson = json.loads(r.data.decode())
            img_url = hjson['img_url']
            cq = "[CQ:image,file=" + img_url + ",id=40000]"
            return f"{AV}的封面图是...\n" + Message(cq)
    except:
        return f"{AV}的封面图未找到\n可能是视频不存在" + AV
