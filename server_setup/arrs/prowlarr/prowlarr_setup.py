from server_setup.arrs.prowlarr.prowlarr_api import *


def main():
    post_indexer()


if __name__ == "__main__":
    if ping_prowlarr():  # Only run main() if Prowlarr API is reachable
        print("Prowlarr API is available.")
        main()
    else:
        print("Prowlarr API is unavailable. Exiting.")
