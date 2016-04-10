from aylienapiclient import textapi
import keys

def summarize(filename, sentences_number = 5):
    client = textapi.Client(keys.aylienid, keys.aylienkey)
    
    f = open(filename, 'r')
    out = open('out.txt', 'w')
    for line in f:
        summary = client.Summarize({'url':line, 'sentences_number':sentences_number})
        out.write('------\n')
        out.write(line + '\n\n')
        for s in summary['sentences']:
            out.write(s.encode("utf-8")+'\n')
        out.write('------\n')

if __name__ == "__main__":
    summarize('in.txt')
