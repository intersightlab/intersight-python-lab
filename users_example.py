import intersight.api.iam_api as iam
import credentials

def main():
    # Configure for authentication
    cred = credentials.config_credentials()
    iapi = iam.IamApi(cred)

    #results = iapi.get_iam_user_list()
    results = iapi.get_iam_user_list()
    print(results)

   

if __name__ == "__main__":
    main()
