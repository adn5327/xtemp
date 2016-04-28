from aylienapiclient import textapi
import keys, csv

def summarize(filename, sentences_number = 5):
    client = textapi.Client(keys.aylienid, keys.aylienkey)
    
    #f = open(filename, 'r')
    out = open('out.txt', 'w')
    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter='^')
        for line in reader:
            summary = client.Summarize({'url':line[1], 'sentences_number':sentences_number})
            out.write('------\n')
            out.write(line[1] + '\n\n')
            out.write(line[0] + '\n\n')
            for s in summary['sentences']:
                out.write(s.encode("utf-8")+'\n')
            out.write('------\n')

if __name__ == "__main__":
    summarize('urls.txt')
