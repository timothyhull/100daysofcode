#!/usr/bin/env python3
import research
import cProfile

profiler = cProfile.Profile()
profiler.disable()


def main():
    print("Weather research for Seattle, 2014-2015")
    print()

    # Enable the profiler
    profiler.enable()

    research.init()

    print("The hottest 5 days:")
    days = research.hot_days()
    for idx, d in enumerate(days[:5]):
        print("{}. {} F on {}".format(idx+1, d.actual_max_temp, d.date))
    print()
    print("The coldest 5 days:")
    days = research.cold_days()
    for idx, d in enumerate(days[:5]):
        print("{}. {} F on {}".format(idx+1, d.actual_min_temp, d.date))
    print()
    print("The wettest 5 days:")

    days = research.wet_days()
    for idx, d in enumerate(days[:5]):
        print("{}. {} inches of rain on {}".format(idx+1, d.actual_precipitation, d.date))

    # Enable the profiler
    profiler.disable()


if __name__ == '__main__':
    for _ in range(1, 25):
        main()

    # Display profiler stats, sorted by cumulative time (cumtime)
    profiler.print_stats(sort='cumtime')
