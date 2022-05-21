import setuptools

if __name__ == "__main__":
    setuptools.setup(
            name = "ToolforMe",
            version = "0.0.7",
            packages = setuptools.find_packages(),
            entry_points = {
                'console_scripts':[
                    'findH = ToolforMe.findH:main',
                    'getmag = ToolforMe.getmag:main',
                    'trim = ToolforMe.trim:main',
                    'POSCARformat = ToolforMe.changePOSCARfile:main',
                    'makeINCAR = ToolforMe.makeINCARfile:main'
                    ],
                },
            )

