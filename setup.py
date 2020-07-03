import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Basic-Email-Templating-Lunarias", # Replace with your own username
    version="0.0.1",
    author="Trent Millar, Jessie Cai",
    author_email="Trent.Millar@nutrien.com, jessie.cai@nutrien.com",
    description="A package that returns a generated HTML email from Jinja2 templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trentmillar/basic-email-templating",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)