import pandas as pd
import matplotlib.pyplot as plt

class Portfolio:
    def __init__(self):
        self.state = {
            'initial_dist': {
                'hdfc': 0.35,
                'icici': 0.2,
                'sbi': 0.15,
                'axis': 0.15,
                'kotak': 0.15
            },
            'initial_investment': 10000,
            'cash': 10000,
            'shares': {}
        }
        self.data = {
            'hdfc': pd.read_csv("data/hdfc.csv", index_col=0, parse_dates=True),
            'icici': pd.read_csv("data/icici.csv", index_col=0, parse_dates=True),
            'sbi': pd.read_csv("data/sbi.csv", index_col=0, parse_dates=True),
            'axis': pd.read_csv("data/axis.csv", index_col=0, parse_dates=True),
            'kotak': pd.read_csv("data/kotak.csv", index_col=0, parse_dates=True)
        }
        self.state['shares'] = {
            'hdfc': self.state['initial_dist']['hdfc'] * self.state['initial_investment'] / self.data['hdfc']["Price"][0],
            'icici': self.state['initial_dist']['icici'] * self.state['initial_investment'] / self.data['icici']["Price"][0],
            'sbi': self.state['initial_dist']['sbi'] * self.state['initial_investment'] / self.data['sbi']["Price"][0],
            'axis': self.state['initial_dist']['axis'] * self.state['initial_investment'] / self.data['axis']["Price"][0],
            'kotak': self.state['initial_dist']['kotak'] * self.state['initial_investment'] / self.data['kotak']["Price"][0]
        }
    def idle_growth(self):
        hdfc_ = self.state['shares']['hdfc'] * self.data['hdfc']["Price"][-1]
        icici_ = self.state['shares']['icici'] * self.data['icici']["Price"][-1]
        sbi_ = self.state['shares']['sbi'] * self.data['sbi']["Price"][-1]
        axis_ = self.state['shares']['axis'] * self.data['axis']["Price"][-1]
        kotak_ = self.state['shares']['kotak'] * self.data['kotak']["Price"][-1]

        hdfc_growth = (hdfc_ / (self.state['initial_dist']['hdfc'] * self.state['initial_investment'])) - 1
        icici_growth = (icici_ / (self.state['initial_dist']['icici'] * self.state['initial_investment'])) - 1
        sbi_growth = (sbi_ / (self.state['initial_dist']['sbi'] * self.state['initial_investment'])) - 1
        axis_growth = (axis_ / (self.state['initial_dist']['axis'] * self.state['initial_investment'])) - 1
        kotak_growth = (kotak_ / (self.state['initial_dist']['kotak'] * self.state['initial_investment'])) - 1

        total_ = hdfc_ + icici_ + sbi_ + axis_ + kotak_

        total_growth = (total_ / self.state['initial_investment']) - 1

        print("HDFC", hdfc_growth * 100)
        print("ICICI", icici_growth * 100)
        print("SBI", sbi_growth * 100)
        print("AXIS", axis_growth * 100)
        print("KOTAK", kotak_growth * 100)
        print("Total", total_growth * 100)

        return total_growth


if __name__ == "__main__":
    portfolio = Portfolio()
    portfolio.idle_growth()
