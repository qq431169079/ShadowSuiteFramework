import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ShadowSuiteFramework",
    version="0.1.2.4",
    author="Shadow Team",
    author_email="public.ShadowTeam@gmail.com",
    description="Shadow Suite Framework is an ethical hacking toolkit/framework.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/Catayao56/ShadowSuiteFramework.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPL License",
        "Operating System :: Linux",
    ),
)
