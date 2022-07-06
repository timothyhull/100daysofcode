#!/usr/bin/env python3
""" Collect user input for the DT FL DB Application. """

# Imports - Python Standard Library
from typing import List, Union

# Imports - Local
from _81.DTFLDB.display_banner import display_banner
from _81.DTFLDB.quit_program import quit_program


def get_new_record_input() -> Union[List[str], None]:
    """ Get user input.

        Args:
            None.

        Returns:
            new_record_input (List):
                namedtuple object containing user input.
    """

    try:
        while True:
            # Display an informational message
            display_banner(
                banner_string='** Add a new DB record **'
            )

            # Create a list of user input data
            new_record_input = []

            # Collect name_input
            while True:
                name_input = input(
                    'Enter a name, or "m" for the Main Menu: '
                )

                # Validate name_input
                if name_input:
                    if name_input == 'm':
                        # Return to the Main Menu
                        return None
                    else:
                        new_record_input.append(name_input)
                        break
                else:
                    print(
                        '\n* Invalid name input *'
                    )
                    continue

            # Collect outbound_interest_score_input
            while True:
                outbound_interest_score_input = input(
                    'Enter an outbound interest score (1-5), '
                    'or "m" for the Main Menu: '
                )

                # Validate outbound_interest_score input
                if outbound_interest_score_input:
                    if outbound_interest_score_input == 'm':
                        # Return to the Main Menu
                        return None
                    else:
                        try:
                            outbound_interest_score_input = int(
                                outbound_interest_score_input
                            )
                        except ValueError:
                            print(
                                '\n* Invalid outbound interest score *'
                            )
                            continue
                        else:
                            if 1 <= outbound_interest_score_input <= 5:
                                new_record_input.append(
                                    outbound_interest_score_input
                                )
                                break
                            else:
                                print(
                                    '\n* Invalid outbound interest score *'
                                )
                                continue

            # Collect inbound_interest_score_input
            while True:
                inbound_interest_score_input = input(
                    'Enter an inbound interest score (1-5), '
                    'or "m" for the Main Menu: '
                )

                # Validate inbound_interest_score_input
                if inbound_interest_score_input:
                    if inbound_interest_score_input == 'm':
                        # Return to the Main Menu
                        return None
                    else:
                        try:
                            inbound_interest_score_input = int(
                                inbound_interest_score_input
                            )
                        except ValueError:
                            print('\n* Invalid inbound interest score *')
                            continue
                        else:
                            if 1 <= inbound_interest_score_input <= 5:
                                new_record_input.append(
                                    inbound_interest_score_input
                                )
                                break
                            else:
                                print(
                                    '\n* Invalid inbound interest score *'
                                )
                                continue

            # Collect num_tries input
            while True:
                num_tries_input = input(
                    'Enter a number of attempts, or "m" for the Main Menu: '
                )

                # Validate num_tries input
                if num_tries_input:
                    if num_tries_input == 'm':
                        # Return to the Main Menu
                        return None
                    else:
                        try:
                            num_tries_input = int(num_tries_input)
                        except ValueError:
                            print(
                                '\n* Invalid number of tries *'
                            )
                            continue
                        else:
                            if num_tries_input >= 0:
                                new_record_input.append(num_tries_input)
                                break
                            else:
                                print(
                                    '\n* Invalid number of tries *'
                                )
                                continue

            # Collect fl_reason input
            while True:
                fl_reason_input = input(
                    'Enter a fl reason, or "m" for the Main Menu: '
                )

                # Validate fl_reason input
                if fl_reason_input:
                    if fl_reason_input == 'm':
                        # Return to the Main Menu
                        return None
                    else:
                        new_record_input.append(fl_reason_input)
                        break

            return new_record_input

    except KeyboardInterrupt:
        # Display a message and exit the application
        quit_program()
