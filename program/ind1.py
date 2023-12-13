#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def add_flight(flights):
    destination = input("Destination name: ")
    aircraft_type = input("Aircraft type: ")
    flight_number = input("Flight number: ")

    flight = {
        'destination': destination,
        'aircraft_type': aircraft_type,
        'flight_number': flight_number,
    }

    flights.append(flight)
    flights.sort(key=lambda item: item.get('flight_number', ''))


def list_flights(flights):
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    print(line)
    print('| {:^4} | {:^30} | {:^20} | {:^8} |'.format("№", "Destination", "Aircraft type", "Flight number"))
    print(line)

    for idx, flight in enumerate(flights, 1):
        print('| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
            idx,
            flight.get('destination', ''),
            flight.get('aircraft_type', ''),
            flight.get('flight_number', '')
        ))

    print(line)


def select_destination(flights, destination_name):
    matching_flights = [flight for flight in flights if flight['destination'] == destination_name]

    if matching_flights:
        print(f"\nFlights to {destination_name}:")
        for flight in matching_flights:
            print(f"Flight Num: {flight['flight_number']}, Aircraft Type: {flight['aircraft_type']}")
    else:
        print(f"\nNo flights found to {destination_name}.")


def help_command():
    print("List of commands:\n")
    print("add - add a flight;")
    print("list - display a list of flights;")
    print("select <destination> - display flight numbers and aircraft types for a destination;")
    print("help - display help;")
    print("exit - exit the program.")


def main():
    flights = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break
        elif command == 'add':
            add_flight(flights)
        elif command == 'list':
            list_flights(flights)
        elif command.startswith('select '):
            destination_name = command.split(' ', maxsplit=1)[1].strip()
            select_destination(flights, destination_name)
        elif command == 'help':
            help_command()
        else:
            print(f"Unknown command {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
