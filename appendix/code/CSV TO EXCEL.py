import pandas as pd


def csv_to_xlsx_pd():
    data = pd.read_csv('fulian4data.csv', encoding='utf-8')
    data_column = list(data.columns)
    data1 = data[[data_column[1],data_column[2],data_column[3],data_column[4],data_column[5],data_column[6],data_column[7],data_column[8],data_column[9]]]
    data1.to_excel('fulian4Date.xlsx')


if __name__ == '__main__':
    csv_to_xlsx_pd()