diagrams = [
    852,843,82,846,1377,1378,1390,1268,1029,1030,262,635,1030,399,403,454,1190,
    584,734,1156,330,320,123,188,46,701,1198,244,911,701,521,932,1181,340,255,
    119,515,1187,717,908,917,258,281,95,520,1025,27,262,793,145,1215,380,775,
    843,343,879,890,892,902,1261,842,618,605,1272,259]
def dia(n):
  myset = set(n)
  return sorted(myset)

print dia(diagrams)