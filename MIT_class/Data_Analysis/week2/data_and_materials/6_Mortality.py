import zipfile
import numpy as np

# returns a 3-tuple of (list of city names, list of variable names, numpy record array with each variable as a field)
def read_mortality_csv(zip_file):
  import io
  import csv
  fields, cities, values = None, [], []
  with io.TextIOWrapper(zip_file.open('data_and_materials/mortality.csv')) as wrap:
    csv_reader = csv.reader(wrap, delimiter=',', quotechar='"')
    fields = next(csv_reader)[1:]
    for row in csv_reader:
	    cities.append(row[0])
	    values.append(tuple(map(float, row[1:])))
    dtype = np.dtype([(name, float) for name in fields])
    return cities, fields, np.array(values, dtype=dtype).view(np.recarray)

with zipfile.ZipFile("MIT_class/Data_Analysis/week2/statsreview_release1.zip") as zip_file:
    m_cities, m_fields, m_values = read_mortality_csv(zip_file)
    
print(m_values)