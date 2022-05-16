import setuptools

if __name__ == "__main__":
    setuptools.setup(
            name = "ToolforMe",
            version = "0.0.4",
            packages = setuptools.find_packages(),
            entry_points = {
                'console_scripts':[
                    'findH = ToolforMe.findH:main',
                    'getmag = ToolforMe.getmag:main',
                    'mCON = ToolforMe.mCON:main'
                    'mCONH = ToolforMe.mCONH:main'
                    'trim = ToolforMe.trim:main'
                    ],
                },
            )

