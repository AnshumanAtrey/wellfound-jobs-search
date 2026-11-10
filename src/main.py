"""Wellfound Jobs Search: the shared job engine (github.com/AnshumanAtrey/ats-jobs-engine) on wellfound.com, the startup job board."""
import asyncio

from ats_jobs.engine import main

if __name__ == '__main__':
    asyncio.run(main('wellfound'))
