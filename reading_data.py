import numpy as np
import pandas as pd
x = []
for l in open("/home/kamnag/Downloads/top-5000-youtube-channels-data-from-socialblade/data.csv"):
    row = l.split(',')
    # print(row)
    x.append(row)
# print(x)
x = np.array(x)
# print(x)

x = pd.read_csv("/home/kamnag/Downloads/top-5000-youtube-channels-data-from-socialblade/data.csv")
print(x.head())
# df = pd.DataFrame(np.random.randn(8, 4), columns=['Rank', 'Grade'])