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

    # Call functions from the research module
    research.init()
    hot_days = research.hot_days()
    cold_days = research.cold_days()
    wet_days = research.wet_days()

    # Disable the profiler
    profiler.disable()

    print("The hottest 5 days:")
    for idx, d in enumerate(hot_days[:5]):
        print("{}. {} F on {}".format(idx+1, d.actual_max_temp, d.date))
    print()

    print("The coldest 5 days:")
    for idx, d in enumerate(cold_days[:5]):
        print("{}. {} F on {}".format(idx+1, d.actual_min_temp, d.date))
    print()

    print("The wettest 5 days:")
    for idx, d in enumerate(wet_days[:5]):
        print("{}. {} inches of rain on {}".format(idx+1, d.actual_precipitation, d.date))


if __name__ == '__main__':
    for _ in range(1, 25):
        main()

    # Display profiler stats, sorted by cumulative time (cumtime)
    profiler.print_stats(sort='cumtime')
