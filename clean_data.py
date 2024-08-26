import pandas as pd
from helper import renaming_dict, strip, data_types

class Data:
    def __init__(self, file):
        self.file = file

        #make a dataframe
        self.df = pd.read_csv(file, index_col="Unnamed: 0", na_values='-')

    def clean(self):
        #drop duplicates
        self.df = self.df.drop_duplicates()

        #drop not important columns
        if "Unnamed" in self.df.columns[-1]:
            number_of_columns = len(self.df.columns)
            self.df = self.df.drop(self.df.columns[-1], axis=1)

        #we don't want player who haven't played
        if "Inns" in self.df.columns:
            self.df = self.df[self.df['Inns'].notna()]

        #if the average goes to infinity, set it to zero
        if "Ave" in self.df.columns:
            self.df['Ave'] = self.df['Ave'].fillna(0)
        
        #separte country from player name
        if 'Country' not in self.df.columns:
            player = self.df['Player'].str.split("(").str[0].apply(str.strip)
            country = self.df['Player'].str.split("(").str[1].apply(strip)
            self.df['Player'] = player
            self.df['Country'] = country

        #strip stars for those which have
        if "HS" in self.df.columns:
            self.df["HS"]=self.df['HS'].str.split("*").str[0]

        #split the span
        if 'Span' in self.df.columns:
            self.df["Debut Year"] = self.df['Span'].str.split("-").str[0]
            self.df["Last Match Year"] = self.df['Span'].str.split("-").str[1]
            self.df = self.df.drop('Span', axis=1)

        if "MD" in self.df.columns:
            self.df["MD"] = self.df.MD.str.split(' ').str[0]

        for column in self.df.columns:
            self.df.astype({column:data_types[column]})

        self.df = self.df.rename(columns=renaming_dict)