import setuptools

setuptools.setup(
    name="py_bleve",
    packages=setuptools.find_packages(include=["py_bleve"]),
    py_modules=["py_bleve.bleve"],
    package_data={"py_bleve": ["*.so"]},
    include_package_data=True,
)
