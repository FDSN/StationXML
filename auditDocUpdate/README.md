### Audit Documentation Changes

Scripts to ensure addition of documentation does not make changes to the
structure of the FDSN StationXML schema. Running compare.sh should produce no
differences if the changes are confined to the documentation.

transform.py uses nodocs.xslt to remove all annotations, then tidy
cleans the output to remove non-structural changes like indentation.
Finally diff shows the raw textual differences between the two versions.

## Install

lxml is used by transform.py, install with:

```
conda install lxml
```

# Run

```
./compare.sh
```

If there are no schema changes besides annotations, the output should look like:

```
% ./compare.sh
Using: fdsn-station-1.1.xsd
Writing transformed XML to fdsn-station-1.1.xsd.nodocs
Writing transformed XML to fdsn-station-local.xsd.nodocs
diff from fdsn-station-local.xsd to fdsn-station-1.1.xsd
< is local tidy version, fdsn-station-local.xsd
> is fdsn tidy version, fdsn-station-1.1.xsd
Note line numbers are in nodocs.tidy,
which will be different from original xsd files.

```
