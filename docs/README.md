# stationxml-doc
StationXML Documentation

## To generate the html/pdf documents

```
make html
```

and/or

```
make latexpdf
```

or running sphinx-build manually

```
sphinx-build -b html . _build/html
```

This will update the html files in _build/html

## Install sphinx

```
conda create -n sphinx python=3.9
conda activate sphinx
conda install sphinx
conda install -c conda-forge sphinxcontrib-contentui
pip install linuxdoc
conda install sphinx_rtd_theme
conda install xmlschema
conda install elementpath
```

## To update ReStructuredText documentation generated from the StationXML schema file

```
python3 convert_xsd_to_rst.py ../fdsn-station.xsd . && make html
```

    or

```
conda run -n sphinx python3 convert_xsd_to_rst.py ../fdsn-station.xsd . && make html
```

This will re-generate the following files from the XSD schema document:
 - level-preamble.rst
 - level-network.rst
 - level-station.rst
 - level-channel.rst
 - level-response.rst
 - warnings.rst

## Spell check
```
pip install sphinxcontrib-spelling
```
which require pyenchant and libenchant.

See https://pyenchant.github.io/pyenchant/install.html

For debian based linux:
```
sudo apt install libenchant-2-2
```
For MacOSX using homebrew (currently does not work on M1 processors):
```
brew install enchant
```

Then add `'sphinxcontrib.spelling'` to `extensions` in conf.py
install libenchant library, see https://pyenchant.github.io/pyenchant/install.html

then run:
```
make spelling
```
output will be in the _build/spelling directory.

## To modify the look and feel of the auto-generated level docs

 The following css divs are described in:
 _static/css/custom.css

  - hatnote - describes the gray box of each element
  - crumb - the navigation trails
  - description - contains the element description
  - type - contains the element type
  - example - contains the element example

Example rst

       <BeginEffectiveTime>
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
       .. container:: hatnote hatnote-gray

       .. container:: crumb

          crumb:Network-->Comment-->BeginEffectiveTime

       .. container:: type

          type::blue:`dateTime`

       .. container:: example

          **Example**: <BeginEffectiveTime>2008-09-15T00:00:00</BeginEffectiveTime>

Hint: If you change the css without changing any .rst files, you must first do:

```
make clean   // deletes all the files in _build/
```

before doing the sphinx-build or it won't take.
