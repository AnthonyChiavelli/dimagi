from __future__ import print_function
import json
import time
import EmailReceiver
import LocationQuerier

MAPS_URL = "http://maps.google.com/maps?q={0},{1}"


def main_loop():
    """
    Listen for emails and output location data
    """

    while True:

        time.sleep(2)

        # Get new emails
        new_emails = EmailReceiver.receive_emails()
        if not new_emails:
            continue

        # Query location specified in emails
        for email in new_emails:

            # Ensure all fields are present
            if len(email) != 3:
                print("Invalid email data")
                continue

            # Extract fields
            from_addr, time_stamp, body = email

            # Make API query with location name
            lat, lng = LocationQuerier.query_location(body)

            # Encode user info and location result into JSON
            # print(json.dumps([from_addr, time_stamp, (lat, lng)]), file=f)
            output_data(from_addr, time_stamp, (lat, lng), show_on_map=False)
            # print(json.dumps([from_addr, time_stamp, (lat, lng)]), file=f)


def output_data(addr, time_stamp, loc, show_on_map=False):
    """
    Take the calculated data (user info and lat/lon) and output it

    :param show_on_map: True to launch google maps with pushpin
        at location
    """
    # Output file
    f = open("output.json", "a")

    # Encode user info and location result into JSON
    print(json.dumps([addr, time_stamp, (loc[0], loc[1])]), file=f)

    if show_on_map:
        import webbrowser
        webbrowser.open(MAPS_URL.format(loc[0], loc[1]), new=2)

if __name__ == "__main__":
    main_loop()