import argparse


def main():
    parser = argparse.ArgumentParser("Job Match AI")
    parser.add_argument("--resume",help="Submit the resume")
    parser.add_argument("--jd",help="Submit the Job Description")
    args = parser.parse_args()
    
    print(f"Resume: {args.resume}")
    
    print(f"JD: {args.jd}")


if __name__ == "__main__":
    main()