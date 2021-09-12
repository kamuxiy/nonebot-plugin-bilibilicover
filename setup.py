import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nonebot_plugin_bilibilicover",
    version="0.0.1",
    author="kamuXiY",
    author_email="1711087540@qq.com",
    description="View the bilibilibili video cover according to BV or AV number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kamuxiy/nonebot-plugin-bilibilicover",
    project_urls={
        "Bug Tracker": "https://github.com/kamuxiy/nonebot-plugin-bilibilicover/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    package_dir={"": "nonebot-plugin-bilibilicover"},
    packages=setuptools.find_packages(where="nonebot-plugin-bilibilicover"),
    python_requires=">=3.6",
)