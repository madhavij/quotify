"""
Script to display Inspirational quotes on Ubuntu Notification tab.

"""
import os
import sys
import random
import subprocess

class Quotify:

    def generate_quote_notification(self):
        """
        Caller function to send desktop notification of quote.
        """
        quotes_file_path = self.get_file_contents("resources/quotes.txt")
        quote = self.get_quote(quotes_file_path)
        self.display_quote(quote)

    def get_file_contents(self,filepath):
        """
        Returns the quotes from file in list.
        """
        lines_list = open(filepath).readlines()
        return lines_list

    def get_quote(self,quotes,seed=None):
        """
        Returns a random quote from the list of text
        """
        random.seed(seed)
        random_quote = random.choice(quotes)
        return random_quote

    def display_quote(self,quote):
        """
        Executes notify command to display quote.
        WARNING: ONLY works on linux distos with notify-send program. Tested on Ubuntu.
        """
        command ='notify-send "Wisdom Dose " '+ quote
        subprocess.Popen(command,shell=True)


def main():
    """
    Entry point for the quotes script.
    """
    quotify = Quotify()
    quotify.generate_quote_notification()

if __name__ =='__main__':
    sys.exit(main())
