import gzip
import pandas as pd
import xml.etree.ElementTree as ET

class Articles():
    def __init__(self, path: str):
        """Read in a pubmed article XML file that is gzipped
        
        Args:
            path (str): location of gzipped file on the disk
        """
        self.article_df = None
        self.author_df = None
        self._parse() # Being inconsistent

    def _parse(self, path: str):
        """Parse the pubmed file"""
        articles = []
        authors = []
        # Trick for creating a dataframe: create list of dicts with same naming format

        with gzip.open(path, 'rb') as fp:
            # _ means throw it away
            for _, article in ET.iterparse(fp, events = ('end',)):
                if article.tag == 'PubmedArticle':
                    article_row, article_authors = self._parse_article(article)
                    articles.append(article_row)
                    articles.extend(article_authors) # Careful extend vs. append

                    # Drop and move on
                    article.clear()
    
        self.article_df = pd.DataFrame(articles)
        self.author_df = pd.DataFrame(authors)

        print(self.article_df.columns)

    def _parse_article(self, article: ET.Element):
        """Parse an XML PubmedArticle element"""
        row = {}
        tags = ['PMID', 'ArticleTitle', 'PubDate', 'DateCompleted', 'Affiliation']
        for el in article.iter():
            if el.tag in tags:
                row[el.tag] = el.text
        
        if 'PMID' not in row.keys():
            return {}, {}
        
        # In XML, there's no rule about order

        authors = []
        tags = ['LastName', 'ForeName', 'Initials', 'Affiliation']
        for author in article.findall('.//Author'):
            auth_row = {'PMID': row['PMID']}
            for el in author.iter():
                if el.tag in tags:
                    auth_row[el.tag] = el.text
            authors.append()

    def get_authors(self):
        """Get parsed grants"""
        return self.author_df
    
    def get_entries(self):
        """Get parsed articles"""
        return self.article_df
    
if __name__ == '__main__':
    articles = Articles('data/pubmed25n1275.xml.gz')