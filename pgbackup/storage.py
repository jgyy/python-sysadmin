def local(infile, outfile):
    outfile.write(infile.read().encode())
    outfile.close()
    infile.close()

