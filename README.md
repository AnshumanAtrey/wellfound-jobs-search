# Wellfound Jobs Scraper & API - AngelList Startup Jobs, Equity

Wellfound jobs scraper and API for wellfound.com, formerly AngelList Talent: search startup jobs by role, place and remote, newest first, and get each job's title, startup, places, remote or office setting, salary and equity, years of experience, startup size, stage and badges, posting date and link. Turn on full details for the description, visa sponsorship, relocation, preferred time zones, skills, the startup's markets and its funding.

Use it as a Wellfound API with no login, an AngelList jobs scraper for remote startup jobs and tech jobs at YC and venture-backed startups, or a daily feed of new startup jobs from the Apify Console, the Apify API, Python, JavaScript, n8n, Make or an AI agent over MCP, and export JSON, CSV or Excel. It reads the public search pages wellfound.com serves to every visitor, every page of each search. Available as an [Apify Actor](https://apify.com/anshumanatrey/wellfound-jobs-search). $0.0027 per job, $0.0029 with full details, $0.005 per run start, no login, no API key.

## What does it do?

- **Reads every page of a Wellfound search, then sorts it newest first.** Wellfound's search pages list startups in its own order, not by date: the newest jobs of a search sit on any of its pages (the 100 newest of the US search were spread over pages 1 to 132 of 167 on 2026-11-10). Wellfound Jobs Scraper reads all of them, so the first rows are the newest jobs of the whole search.
- **Startup data on every row.** Pay and equity as Wellfound shows them, parsed into numbers with their currency; the startup's size, stage (early, growth, scale, public) and badges such as YC Funded, Top Investors, Valuation $1B+ and Recently funded; the remote setting in Wellfound's own words and the countries a remote job hires in.
- **One job title is enough.** Type software engineer and press Start. Wellfound's 518 roles are matched for you, and a title no role fits is found in every job. Leave the form empty for the newest jobs on all of Wellfound.
- **Places the way people type them.** San Francisco, NYC, Bangalore or Bengaluru, California, Germany, Europe, EMEA, Remote India or Worldwide. Wellfound's own place pages hold every town inside a country or region, and a job read from one is matched to it even when its own town is a small one.
- **Filters startup job seekers use.** Remote, hybrid or onsite, job type, years of experience, lowest yearly pay in any currency, and startup stage.
- **Full details from each job's page.** Visa sponsorship, relocation, preferred time zones, skills, the startup's website, markets and funding (amount raised, number of rounds, newest round and its month), and every place with its region and country.
- **Checks job links.** Paste Wellfound job links, and each comes back open, closed (taken down) or not found.

## How is it different from other Wellfound scrapers?

- **Newest first across the whole search.** The other Wellfound actors read the first 1 to 10 pages of a search by default, in Wellfound's own order, and sort only what they read. On 2026-11-10 the software engineer search had 89 pages, and its 100 newest jobs were on 46 of them, from page 1 to page 84.
- **No proxy by default.** Wellfound's search pages answer plain requests, so Wellfound Jobs Scraper reads them with no proxy; the most used Wellfound actors default to a paid US residential proxy, billed on top of their prices.
- **Honest counts.** Wellfound shows visitors at most 3 jobs of each startup in a search. Every run says how many jobs Wellfound lists for your search and how many it shows, so you know what a search on Wellfound itself can reach.
- **Typed words, not URLs.** A job title, a place and a filter are enough; a pasted Wellfound search link works too.
- **You pay for what you get.** One charge per delivered row, plus the run start, and a spending limit stops the run cleanly with the jobs it paid for.

Every actor on the Apify Store that names Wellfound or AngelList in its title or slug and had 40 or more users in the last 30 days on 2026-11-10, ordered by users, as each one's listing and input form state it:

| Feature | blackfalcondata | memo23 | clearpath | orgupdate | gio21 | radeance | This actor |
|---|---|---|---|---|---|---|---|
| Users, 30 days | 492 | 155 | 119 | 54 | 53 | 44 | new |
| What you type | A keyword, roles or search links | Search links or a keyword | Search links | Keyword and city | Keyword | Role and city slugs | A job title, a place, or nothing |
| Pages read by default | 10 | up to 1,000 jobs | 1 | 1 | 5 | 1 | every page of the search |
| Newest first | no | optional, within the jobs read | within the pages read | no | no | within the pages read | across every page |
| Proxy by default | US residential | residential | residential recommended | none stated | none stated | none stated | none |
| Pay or equity filter | yes | jobs without pay | no | no | funding stage | yes | yes, and startup stage |
| Job link check: open, closed or not found | no | no | no | no | no | no | yes |

## When should I use it?

- **Job seekers and job boards:** new startup jobs by title, city, remote setting, pay and equity, newest first, on a daily schedule.
- **Recruiters and talent teams:** which startups are hiring for a role right now, at what stage, size and pay.
- **Sales and venture research:** startups hiring as a buying signal, by market, stage and funding, with their websites.
- **Data teams and AI agents:** one clean, stable feed of Wellfound jobs through the API or MCP.

## How much does it cost to scrape Wellfound jobs?

Pay per event: $2.70 per 1,000 jobs, or $2.90 per 1,000 with full details, plus $0.005 per run. Apify's free $5 monthly credit covers about 1,800 jobs in runs of 100. Platform usage is included, and there is no monthly fee.

| Event | Price | When it is charged |
|---|---|---|
| Job | $0.0027 | One saved job, and one checked link that is closed or not found |
| Job with details | $0.0029 | One saved job with full details on |
| Run start | $0.005 per GB of memory | Charged by Apify when a run starts: once up to 1 GB and once more for each extra GB, so $0.005 at the default 1 GB |

| Run (default memory) | Cost |
|---|---|
| 100 newest jobs | $0.275 |
| 100 jobs with full details | $0.295 |
| 1,000 jobs | $2.705 |

Number of jobs (`maxJobs`) and the run start set the most a run can cost, and a run stops at its spending limit with a message saying so.

## How does the price compare with other Wellfound scrapers?

Every actor on the Apify Store that names Wellfound or AngelList in its title or slug and had 40 or more users in the last 30 days, found by searching the Store for 8 Wellfound and AngelList terms on 2026-11-10 (159 actors read), ordered by users. Free-plan prices from each actor's current pricing.

| Actor | Users, 30 days | Per job | Start fee | Proxy |
|---|---|---|---|---|
| blackfalcondata/wellfound-scraper | 492 | $0.003 | $0.005 | US residential by default, billed on top |
| memo23/wellfound-jobs-scraper | 155 | $0.00099, plus $0.0015 for job details | $0.01 | residential by default |
| clearpath/wellfound-api-ppe | 119 | $0.00299 | $0.00005 | residential recommended |
| orgupdate/wellfound-jobs-scraper | 54 | $0.005 | $0.002 | none stated |
| gio21/wellfound-jobs-scraper | 53 | $0.003 | none | none stated |
| radeance/wellfound-job-listings-scraper | 44 | $0.01 | $0.001 | none stated |
| This actor | new | $0.0027, $0.0029 with details | $0.005 | none |

Where others are cheaper: memo23 costs less per job when you need no details, and a run that saves only a few jobs costs less on actors with a smaller start fee (clearpath, gio21, radeance). Where others do more: blackfalcondata, memo23 and clearpath can deliver only the jobs new since your last run and send alerts; memo23 and radeance add company profiles, and memo23 contact emails.

## Which inputs does it take?

Nothing is required. Type a job title and press Start, or press Start with the form empty.

| Field | What it does |
|---|---|
| Job titles to find (`searchTerms`) | One per line, such as software engineer or product designer. Wellfound's own role pages are read, and a job matches when its title has every word. A pasted Wellfound search link works too |
| Where the job is (`location`) | Cities, US states, countries or regions: San Francisco, NYC, Bangalore, California, Germany, Europe, EMEA. Remote alone asks for remote jobs, Remote India for remote jobs open to India, Worldwide for jobs open anywhere |
| Remote or office (`workType`) | remote, hybrid or onsite, as Wellfound marks the job |
| Job type (`employmentType`) | full-time, part-time, contract or intern; empty keeps every type, cofounder roles included |
| Posted in the last (`postedWithin`) | 24 hours, 3 days, 7 days, 30 days (the default), any time, or your own period such as 48 hours |
| Number of jobs (`maxJobs`) | How many, newest first: 100 by default, 0 for every match |
| Full details (`includeDetails`) | Adds the description, visa sponsorship, relocation, time zones, skills, the startup's website, markets and funding, and the city, region and country |
| Leave out words (`excludeTerms`) | Drops jobs whose title has these words, such as senior or intern |
| Lowest yearly pay (`minSalary`) | Keeps jobs whose pay range reaches it, in its currency: 150k USD, 20L INR, 60000 EUR |
| Company stage (`companyStage`) | early, growth, scale or public, as Wellfound marks the startup |
| Experience (`experienceYears`) | Your years: 3, 2-5, 5+ or fresher; a job is kept when the fewest years it asks for is within yours |
| Descriptions too (`searchDescriptions`) | Finds your words in each job's description too, not only the title |
| Only these startups (`companies`) | Startup names or Wellfound company links, found among the jobs the run reads |
| Job links to check (`jobUrls`) | Paste job links to check whether they are still open, instead of searching |
| Connection (`proxyConfiguration`) | Leave it off; turn on Apify Proxy only when a run says Wellfound refused the address |

Example input:

```json
{
  "searchTerms": ["software engineer"],
  "location": ["New York City", "Remote"],
  "minSalary": "150k USD",
  "postedWithin": "7 days",
  "maxJobs": 100
}
```

## What does the output look like?

One row per job, newest first. These rows are from a run of the example input (software engineer) on 2026-11-10: Wellfound listed 4,836 jobs for the search and showed 2,649; 266 had both words in the title and went live in the last 30 days, and the 100 newest were saved in 7 s.

| Job title (`title`) | Startup name (`company`) | Main location (`location`) | Remote or office (`workType`) | Pay summary (`salary`) | Posted on (`postedAt`) |
|---|---|---|---|---|---|
| GIS Software Engineer | EdgeQ Technologies | New York City | remote | USD 75,000 - 135,000 per year | 2026-11-10 |
| Full Stack Software Engineer | Moongate | Hong Kong | remote | USD 70,000 - 80,000 per year | 2026-11-10 |
| Staff Software Engineer | FlowGen Labs | San Francisco | onsite | USD 225,000 - 450,000 per year | 2026-11-10 |
| Staff Software Engineer (Applied AI) | Traba | New York City | onsite | USD 240,000 - 300,000 per year | 2026-11-10 |
| Software Engineer, iOS | Mirage | New York | onsite | USD 175,000 - 275,000 per year | 2026-11-10 |

One row as JSON:

```json
{
  "title": "Staff Software Engineer (Applied AI)",
  "company": "Traba",
  "location": "New York City",
  "otherLocations": ["San Francisco"],
  "workType": "onsite",
  "employmentType": "full-time",
  "salary": "USD 240,000 - 300,000 per year",
  "postedAt": "2026-11-10T00:37:18Z",
  "jobUrl": "https://wellfound.com/jobs/5027476-staff-software-engineer-applied-ai",
  "applyUrl": "https://wellfound.com/jobs/5027476-staff-software-engineer-applied-ai",
  "status": "open",
  "platform": "wellfound",
  "companySlug": "traba-work",
  "companyWebsite": null,
  "jobId": "5027476",
  "checkedAt": "2026-11-10T10:59:28+00:00",
  "experienceMin": null,
  "experienceMax": null,
  "salaryMin": 240000,
  "salaryMax": 300000,
  "salaryCurrency": "USD",
  "salaryPeriod": "year",
  "offersEquity": true,
  "equityMin": 0.13,
  "equityMax": 0.24,
  "remoteIn": [],
  "remotePolicy": null,
  "role": "Software Engineer",
  "companySize": "51-200",
  "companyStage": null,
  "companyTagline": "Making the supply chain operate at peak efficiency",
  "companyBadges": ["Actively Hiring", "Growing fast"]
}
```

Full details add `description`, `descriptionHtml`, `visaSponsorship`, `relocation`, `timezones`, `skills`, `industries`, `companyWebsite`, `companyLocation`, `companyFunding`, `fundingRounds`, `latestRound`, `latestRoundDate`, `reposted`, `city`, `region`, `country` and `countryCode`. On 2026-11-10, Cooklist's machine learning engineer job came back with visa sponsorship not available, relocation allowed, Python and Machine Learning as skills, six markets, $3M raised in 1 round, and Austin, Texas, United States. A checked link that is closed or not found comes back with its `status`, the startup when the page names it, and the link. A run also writes an `OUTPUT` record: the Wellfound search pages read, how many jobs they list and show, how many matched and were saved, any notes on how your input was read, and the settings used.

## How fast is it?

Seconds for a role or a city, about a minute for all of Wellfound. Measured on 2026-11-10 from a laptop: the example input read 89 pages in 7 s; product manager in New York City 11 pages in 4 s; the empty form, every job on Wellfound, 578 pages in 51 s with a 246 MB memory peak; every job with no date limit, 12,460 rows in 57 s. Full details read each saved job's page once more: 9 remote machine learning jobs with details took 6 s.

## Common questions

### Is Wellfound the same as AngelList?

Yes. Wellfound is the job site that was called AngelList Talent (angel.co/jobs) until 2022, with the same startups and the same job pages; old angel.co job links lead to wellfound.com. Wellfound Jobs Scraper reads wellfound.com and accepts angel.co job links in Job links to check (`jobUrls`).

### Why does it read every page of a search?

Wellfound's search pages list startups in Wellfound's own order, not by date, and that order changes while you read it. Reading every page is the only way to know which jobs of a search are the newest, so Wellfound Jobs Scraper reads them all and sorts the jobs by the moment each went live. A job that comes twice while the order changes is kept once.

### Why does Wellfound show only some of a search's jobs?

Wellfound shows visitors at most 3 jobs of each startup in a search: on 2026-11-10 its software engineer search listed 4,836 jobs and showed 2,649. Wellfound Jobs Scraper reads every job a search shows, says both numbers in each run's message, and reaches more of a startup's jobs when the search is narrower: a role at a place shows up to 3 of that startup's jobs there.

### Which posting date does it use?

Wellfound Jobs Scraper uses the moment a job went live on Wellfound, to the second, which is also the date in the job page's own markup (10 of 10 links checked in each run). A reposted job counts from the day it went up again, as Wellfound shows it ("Reposted: today"); with full details, `reposted` says which jobs those are.

### How are job titles matched?

Wellfound Jobs Scraper reads Wellfound's own role pages for what you type: software engineer reads the Software Engineer role, senior python developer the Python Developer role, react the React Developer and React Native roles, and marketing Wellfound's marketing page. A job then matches when its title has every word you typed, so frontend also finds Front-End. Tick Descriptions too (`searchDescriptions`) to find your words in the descriptions as well. A title no role fits, such as llm, is looked for in every job on Wellfound (or at your places), which takes about a minute.

### How do places work?

Wellfound has a page for 475 places: cities, US states, countries and regions. Wellfound Jobs Scraper reads the page of each place you type, and a country's page holds every town in it: on 2026-11-10 India's page held jobs in Sonipat, Vellore and HSR Layout. Bengaluru and Bangalore, NYC and New York City, SF and San Francisco all work, a region such as EMEA or APAC reads Wellfound's pages for its continents and countries, and an Indian town with no page of its own reads its state's.

### What does remote mean on Wellfound?

Wellfound Jobs Scraper calls a job remote when Wellfound marks it remote: remote only, onsite or remote, or remote with no policy set. Hybrid is in office with work-from-home flexibility, and onsite is in office. `remotePolicy` gives Wellfound's own words, and `remoteIn` the countries, regions or towns a remote job hires in, or Everywhere. Remote India in Where the job is (`location`) keeps remote jobs that hire in India or everywhere; Worldwide keeps those that hire everywhere.

### How does years of experience work?

Wellfound states the fewest years a job asks for, on about 6 jobs in 10 (64% of 12,460 jobs on 2026-11-10), and rarely a most. Type your years in Experience (`experienceYears`), such as 3, and Wellfound Jobs Scraper keeps the jobs that ask for 3 years or fewer; 2-5 keeps those that ask for 5 or fewer, and fresher those that need no experience. A job that states no years is left out once you set this.

### How do the pay and equity fields work?

Wellfound Jobs Scraper reads the pay and equity Wellfound shows, such as $175k to $215k with 0.5% to 1% equity, into `salaryMin`, `salaryMax`, `salaryCurrency`, `equityMin` and `equityMax`. Wellfound asks startups for yearly pay, so `salaryPeriod` is year; a few type a monthly figure there. Pay was shown on 64% of jobs on 2026-11-10 and an equity range on 15%. Lowest yearly pay (`minSalary`) keeps the jobs whose range reaches your amount in that currency.

### What if a search finds nothing?

Wellfound Jobs Scraper says why in the run's message and in its `OUTPUT` record, and charges only the run start. When jobs with your words were left out by a filter, it names the filter that left them out and how to loosen it; when your place has no such jobs on Wellfound, it says Wellfound has no job with your words inside your other filters. The message also shows how your input was read, such as which roles and place pages were used.

### Does it need a login, a proxy or an API key?

Wellfound Jobs Scraper needs no Wellfound login, no proxy and no API key, because it reads the public search pages wellfound.com serves to every visitor. Wellfound's Cloudflare check refused one address for about 7 minutes after some 1,500 pages from it in 15 minutes (measured on 2026-11-10); a run that meets it slows down, waits, and then saves what it read and says so. Turn on Apify Proxy in Connection (`proxyConfiguration`) only if a run says so.

### Does it work on Apify's free plan?

Wellfound Jobs Scraper works on Apify's free plan: $0.0027 a job plus the $0.005 run start. The free $5 monthly credit pays for about 1,800 jobs in runs of 100.

### How often should I run it?

Running Wellfound Jobs Scraper once a day keeps a startup job feed fresh: set Posted in the last (`postedWithin`) to 24 hours and Number of jobs (`maxJobs`) to 0 to get every job that went live that day: 202 in the 24 hours before a run on Monday 2026-11-10. Set the run up under Schedules in Apify Console, and match rows on `jobId` to skip jobs you already have.

### How do I check a list of job links?

Wellfound Jobs Scraper checks whether Wellfound job links are still open when you paste them into Job links to check (`jobUrls`), one per line, instead of searching. Each link comes back as one row: open with the job's fields from its page, closed when Wellfound has taken it down, or not found.

### How do I call it from the API, Python, JavaScript, n8n or an AI agent?

Wellfound Jobs Scraper runs from the Apify API, Python, JavaScript, n8n, Make or an AI agent over MCP. Each way uses your Apify token (Apify Console, Settings, API & Integrations) and takes the input as JSON keyed by the field names, such as `searchTerms` and `maxJobs`.

**API.** One call runs the actor and returns its rows. Apify stops that wait after 300 seconds, which covers any search; a client below waits as long as a run takes.

```bash
curl -X POST "https://api.apify.com/v2/acts/anshumanatrey~wellfound-jobs-search/run-sync-get-dataset-items" \
  -H "Authorization: Bearer <YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"searchTerms": ["software engineer"]}'
```

**Python** (`pip install apify-client`):

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("anshumanatrey/wellfound-jobs-search").call(run_input={"searchTerms": ["software engineer"]})
for row in client.dataset(run.default_dataset_id).iterate_items():  # apify-client 3+; on 2.x use run["defaultDatasetId"]
    print(row["title"], row["company"], row["location"], row["salary"], row["equityMin"], row["jobUrl"])
```

**JavaScript** (`npm install apify-client`):

```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: '<YOUR_APIFY_TOKEN>' });
const run = await client.actor('anshumanatrey/wellfound-jobs-search').call({ searchTerms: ['software engineer'] });
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) console.log(row.title, row.company, row.location, row.salary, row.equityMin, row.jobUrl);
```

**n8n and Make.** In n8n, add the Apify node, pick Run an Actor and get dataset, choose this actor and paste the input JSON: the rows come out as n8n items. In Make, the Apify app's Run an Actor and Get Dataset Items modules do the same.

**AI agents (MCP).** Add `https://mcp.apify.com?tools=anshumanatrey/wellfound-jobs-search` to your MCP client and sign in with Apify, or send `Authorization: Bearer <YOUR_APIFY_TOKEN>`. The agent gets this actor as a tool and sees every input field by its JSON key.

### Am I charged for closed jobs?

Wellfound Jobs Scraper charges for a closed job only when you paste its link to check. A search returns open jobs, and a pasted link that turns out closed or not found is one Job row, because it was checked and answered.

### Is it legal to use?

Wellfound Jobs Scraper reads public job postings that Wellfound shows to every visitor. You are responsible for how you use the data, including Wellfound's terms and the privacy laws that apply to you. Wellfound Jobs Scraper is not made or endorsed by Wellfound; the Wellfound name and logo identify the site it reads.

## Limitations

- Wellfound shows visitors at most 3 jobs of each startup in a search; a startup's other jobs there are not on its search pages, and its own company page sits behind a browser check this actor does not pass.
- Wellfound's order shifts while a search is read, so one read sees about 95% of a search's startups (452 of 463 in a measured search); a job that comes twice is kept once.
- Pay is shown on 64% of jobs, an equity range on 15%, years of experience on 64% and a startup stage on 43% (12,460 jobs, 2026-11-10).
- A sign several currencies share (¥, ₨, kr) gives no currency on a search row; full details read it from the job page.
- Visa sponsorship, relocation, time zones, skills, markets and funding come with full details only, one more page per job.
- A title no Wellfound role fits, and a place with no Wellfound page, read every job on Wellfound, about a minute.
- Wellfound's Cloudflare check refused one address for about 7 minutes after some 1,500 pages in 15 minutes (2026-11-10). A run that meets it saves what it read and says so.

## Who maintains it?

Built and maintained by **Anshuman Atrey** ([@AnshumanAtrey](https://github.com/AnshumanAtrey)), who publishes a portfolio of data and OSINT actors on Apify Store. For a feature request or a bug, message [LinkedIn](https://linkedin.com/in/anshumanatrey) (fastest), open an issue on the GitHub repo, or write through [atrey.dev](https://atrey.dev).

## Sibling actors

| Actor | What it searches |
|---|---|
| [Greenhouse Jobs Scraper](https://apify.com/anshumanatrey/greenhouse-jobs-search) | Jobs from every company on Greenhouse, searched live |
| [Lever Jobs Scraper](https://apify.com/anshumanatrey/lever-jobs-search) | Jobs from 2,300+ companies on Lever (jobs.lever.co), searched live |
| [Ashby Jobs Scraper](https://apify.com/anshumanatrey/ashby-jobs-search) | Jobs from every company on Ashby (jobs.ashbyhq.com), where many startups post |
| [Workday Jobs Scraper](https://apify.com/anshumanatrey/workday-job-search) | Jobs from every company on Workday (myworkdayjobs.com), searched live |
| [SmartRecruiters Jobs Scraper](https://apify.com/anshumanatrey/smartrecruiters-jobs-search) | Jobs from 2,900+ companies on SmartRecruiters, searched live |
| [Workable Jobs Scraper](https://apify.com/anshumanatrey/workable-job-search) | Jobs from every company on Workable, in one search |
| [Deel Jobs Scraper](https://apify.com/anshumanatrey/deel-jobs-search) | Jobs from every company on Deel ATS (jobs.deel.com), with pay |
| [Cornerstone Jobs Scraper](https://apify.com/anshumanatrey/cornerstone-jobs-search) | Jobs from every company on Cornerstone (csod.com), searched live |

For the people behind a company: [LinkedIn Profile Finder](https://apify.com/anshumanatrey/linkedin-harvester) turns an email into a public LinkedIn profile.

## Documentation

- Apify Store: https://apify.com/anshumanatrey/wellfound-jobs-search
- GitHub repo: https://github.com/AnshumanAtrey/wellfound-jobs-search (MIT license, see [LICENSE](LICENSE))
- The engine behind it: https://github.com/AnshumanAtrey/ats-jobs-engine

## Last updated

2026-11-10 (version 1.0)
