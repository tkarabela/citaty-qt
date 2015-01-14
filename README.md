# Citáty

Simple quote-of-the-day app in Python and Qt. It's got slightly more brains than `random.choice(quotes)` and runs as a standalone app on Windows. That's it.

For quote-of-the-day in the browser, have a look at <https://github.com/tkarabela/citaty>.

## Requirements

- Python 2.7
- PySide
- cx_Freeze

## How to use it

1. Run `build.bat`.
2. The `dist` directory contains all you need to run the app.
3. To get your quote of the day, run `dist/citaty.exe`.
4. To add quotes, edit `dist/citaty.txt`, one line per quote, UTF-8 with BOM.

## License

Copyright (c) 2015 Tomas Karabela

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
