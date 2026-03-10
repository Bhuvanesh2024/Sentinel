# tirreno

<div align="center" style="background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); padding: 20px; border-radius: 10px;">

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ec30c28f67de476f8b98d2798079bdf0)](https://app.codacy.com/gh/TirrenoTechnologies/tirreno/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Docker Pulls](https://img.shields.io/docker/pulls/tirreno/tirreno?style=flat)](https://hub.docker.com/r/tirreno/tirreno/)
[![Research](https://img.shields.io/badge/Research-Papers-9cf?style=flat&logo=academia)](https://github.com/tirrenotechnologies/tirreno#research-papers)
[![License](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

</div>

<p align="center">
    <a href="https://www.tirreno.com/" target="_blank">
        <img src="https://www.tirreno.com/firstscreen.jpg" alt="tirreno screenshot" />
    </a>
</p>

[tirreno](https://www.tirreno.com) is an open-source security framework.

tirreno *[tir.ˈrɛ.no]* helps understand, monitor, and protect your product from threats, fraud, and abuse. While classic cybersecurity focuses on infrastructure and network perimeter, most breaches occur through compromised accounts and application logic abuse that bypasses firewalls, SIEM, WAFs, and other defenses. tirreno detects threats where they actually happen: inside your product.

tirreno is a few-dependency, "low-tech" PHP/PostgreSQL application. After a straightforward five-minute installation, you can ingest events through API calls and immediately access a real-time threat dashboard.

## Core components
* **SDKs & API** Integrate tirreno into any product with SDKs.
  Send events with full context in a few lines of code.
* **Built-in dashboard** Monitor and understand your product's
  security events from a single interface. Ready for use in minutes.
* **Single user view** Analyze behaviour patterns, risk scores,
  connected identities, and activity timelines for a specific user.
* **Rule engine** Calculate risk scores automatically with preset
  rules or create your own customized for your product.
* **Review queue** Automatically suspend accounts with risky events
  or flag them for manual review through threshold settings.
* **Field audit trail** Track modifications to important fields,
  including what changed and when to streamline audit and compliance.

## Preset rules

`Account takeover` `Credential stuffing` `Content spam` `Account registration` `Fraud prevention` `Insider threat`
`Bot detection` `Dormant account` `Multi-accounting` `Promo abuse` `API protection` `High-risk regions`

## Built for

* **Self-hosted, internal and legacy apps**: Embed security layer
  to extend your security through audit trails, protect user accounts
  from takeover, detect cyber threats and monitor insider threats.
* **SaaS and digital platforms**: Prevent cross-tenant data leakage,
  online fraud, privilege escalation, data exfiltration and business
  logic abuse.
* **Mission critical applications**: Sensitive application protection,
  even in air-gapped deployments.
* **Industrial control systems (ICS) and command & control (C2)**: Protect,
  operational technology, command systems, and critical infrastructure
  platforms from unauthorized access and malicious commands.
* **Non-human identities (NHIs)**: Monitor service accounts, API keys,
  bot behaviors, and detect compromised machine identities.
* **API-first applications**: Protect against abuse, rate limiting
  bypasses, scraping, and unauthorized access.

## Live demo

Check out the live demo at [play.tirreno.com](https://play.tirreno.com) (*admin/tirreno*).

## Requirements

* **PHP**: Version 8.0 to 8.3
* **PostgreSQL**: Version 12 or greater
* **PHP extensions**: `PDO_PGSQL`, `cURL`
* **HTTP web server**: `Apache` with `mod_rewrite` and `mod_headers` enabled
* **Operating system**: A Unix-like system is recommended
* **Minimum hardware requirements**:
  * **PostgreSQL**: 512 MB RAM (4 GB recommended)
  * **Application**: 128 MB RAM (1 GB recommended)
  * **Storage**: Approximately 3 GB PostgreSQL storage per 1 million events

## Docker-based installation

To run tirreno within a Docker container you may use command below:

```bash
curl -sL tirreno.com/t.yml | docker compose -f - up -d
```
Continue with step 4 of [Quickstart](#quickstart-install).

## Quickstart install
1. [Download](https://www.tirreno.com/download.php) the latest version of tirreno (ZIP file).
2. Extract the tirreno-master.zip file to the location where you want it installed on your web server.
3. Navigate to `http://localhost:8585/install/index.php` in a browser to launch the installation process.
4. After the successful installation, delete the `install/` directory and its contents.
5. Navigate to `http://localhost:8585/signup/` in a browser to create an administrator account.
6. For cron job setup, insert the following schedule (every 10 minutes) expression with the `crontab -e` command or by editing the `/var/spool/cron/your-web-server` file:

```
*/10 * * * * /usr/bin/php /absolute/path/to/tirreno/index.php /cron
```

## Using Heroku (optional)

Click [here](https://heroku.com/deploy?template=https://github.com/tirrenotechnologies/tirreno) to launch heroku deployment.

## Via Composer and Packagist (optional)

tirreno is published at Packagist and could be installed with Composer:

```
composer create-project tirreno/tirreno
```

or could be pulled into an existing project:

```
composer require tirreno/tirreno
```

## SDKs

* [PHP](https://github.com/tirrenotechnologies/tirreno-php-tracker)
* [Python](https://github.com/tirrenotechnologies/tirreno-python-tracker)
* [NodeJS](https://github.com/tirrenotechnologies/tirreno-nodejs-tracker)

## Documentation

See the [User guide](https://docs.tirreno.com/) for details on how to use tirreno, [Developers documentation](https://github.com/tirrenotechnologies/DEVELOPMENT.md) to customize your integration, [Admin documentation](https://github.com/tirrenotechnologies/ADMIN.md) for installation, maintenance and updates.

## Research Papers

tirreno's approach to behavioral analytics and threat detection is grounded in academic research and industry best practices:

### Core Research Foundation

**1. User Behavior Analytics for Attack Detection**
- 📄 [User Behavior Analytics for HTTP-GET Flood Attack Detection](https://www.researchgate.net/publication/User_Behavior_Analytics_for_HTTP-GET_Flood_Attack_Detection)
  - *Focus*: Behavioral pattern analysis for detecting volumetric attacks
  - *Relevance*: Foundation for tirreno's velocity-based detection rules

**2. AI-Driven Behavioral Analytics**
- 📄 [AI-Driven Behavioral Analytics for Web Application Intrusion Detection Systems: A Machine Learning Approach to Anomaly Detection](https://www.researchgate.net/publication/392369007_AI-Driven_Behavioral_Analytics_for_Web_Application_Intrusion_Detection_Systems_A_Machine_Learning_Approach_to_Anomaly_DetectionAI-Driven)
  - *Focus*: Machine learning techniques for web application security
  - *Relevance*: Informs tirreno's anomaly detection algorithms and risk scoring mechanisms

**3. Web Application Security Architecture**
- 📄 [Research on Web Application Security Detection Technology (Scientific.net)](https://www.scientific.net/AMM.411-414.607)
  - *Focus*: Security detection methodologies for web applications
  - *Relevance*: Architectural principles for application-layer threat detection

**4. Intrusion Detection Systems**
- 📄 [Computer & Security Journal - Web Application Intrusion Detection](https://www.sciencedirect.com/science/article/abs/pii/S1084804518301176)
  - *Focus*: Advanced intrusion detection techniques for web applications
  - *Relevance*: Multi-layered detection approach and real-time analysis strategies

### Key Research Areas Applied in tirreno

- **Behavioral Pattern Recognition**: Analyzing user activity sequences to identify anomalies
- **Real-Time Threat Intelligence**: Sub-second event processing and risk calculation
- **Identity Correlation**: Graph-based analysis of connected accounts and shared attributes
- **Adaptive Risk Scoring**: Dynamic threshold adjustment based on contextual factors
- **Application-Layer Security**: Focus on business logic abuse and account compromise

### Contributing Research

We welcome academic collaboration and research partnerships. If you're conducting research in behavioral security analytics, fraud detection, or application security, please reach out to research@tirreno.com.

## About

tirreno is an open-source security framework that embeds protection against threats, fraud, and abuse right into your product.

The project started as a proprietary system in 2021 and was open-sourced (AGPL) in December 2024.

Behind tirreno is a blend of extraordinary engineers and professionals, with over a decade of experience in cyberdefence. We solve real people's challenges through love in *ascétique* code and open technologies. tirreno is not VC-motivated. Our inspiration comes from the daily threats posed by organized cybercriminals, driving us to reimagine the place of security in modern applications.

## Why the name tirreno?

Tyrrhenian people may have lived in Tuscany and eastern Switzerland as far back as 800 BC. The term "Tyrrhenian" became more commonly associated with the Etruscans, and it is from them that the Tyrrhenian Sea derives its name, which is still in use today.

According to historical sources, Tyrrhenian people were the first to use trumpets for signaling about coming threats, which was later adopted by Greek and Roman military forces.

While working on the logo, we conducted our own historical study and traced mentions of 'tirreno' back to the 15th-century printed edition of the Vulgate (the Latin Bible). We kept it lowercase to stay true to the original — quite literally, by the book. The tirreno wordmark stands behind the horizon line, as a metaphor of the endless evolutionary cycle of the threat landscape and our commitment to rise over it.

## Links

* [Website](https://www.tirreno.com)
* [Live demo](https://play.tirreno.com)
* [Admin documentation](https://github.com/tirrenotechnologies/ADMIN.md)
* [Developers documentation](https://github.com/tirrenotechnologies/DEVELOPMENT.md)
* [User guide](https://docs.tirreno.com)
* [Mattermost community](https://chat.tirreno.com)

## Reporting a security issue

If you've found a security-related issue with tirreno, please email security@tirreno.com. Submitting the issue on GitHub exposes the vulnerability to the public, making it easy to exploit. We will publicly disclose the security issue after it has been resolved.

After receiving a report, tirreno will take the following steps:

* Confirm that the report has been received and is being addressed.
* Attempt to reproduce the problem and confirm the vulnerability.
* Release new versions of all the affected packages.
* Announce the problem prominently in the release notes.
* If requested, give credit to the reporter.

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License (AGPL) as published by the Free Software Foundation version 3.

The name "tirreno" is a registered trademark of tirreno technologies sàrl, and tirreno technologies sàrl hereby declines to grant a trademark license to "tirreno" pursuant to the GNU Affero General Public License version 3 Section 7(e), without a separate agreement with tirreno technologies sàrl.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see [GNU Affero General Public License v3](https://www.gnu.org/licenses/agpl-3.0.txt).

## Authors

tirreno Copyright (C) 2026 tirreno technologies sàrl, Vaud, Switzerland. (License AGPLv3)

't'
