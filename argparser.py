import argparse
subparse = argparse.ArgumentParser(description="CLI for finding and starting pipeline")
subparse.add_argument("grpid", help="contains group id of package")
subparse.add_argument("artid", help="contains group id of artifact")
subparse.add_argument("--version", help="contains version")
args=subparse.parse_args()
print(args.grpid)
print(args.artid)
print(args.version)
