import requests


def get_announcement_text(ctl_num):
    return requests.get(f'https://data.usajobs.gov/api/historicjoa/announcementtext/{ctl_num}').json()


def get_announcements_duties():
    majorpath = '12andLower.txt'
    with open(majorpath, 'r') as f:
        control_numbers = [line.strip().split()[1] for line in f]


    for ctl_num in control_numbers:
        response = get_announcement_text(ctl_num)
        if 'duties' in response:
            duties_list = response['duties']
            #duties_list = response['majorDutiesList']
            print(duties_list)
        else:
            print(f"No majorDutiesList found for control number: {ctl_num}")


if __name__ == "__main__":
    get_announcements_duties()
