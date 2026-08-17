---
title: "user-agent"
---

# user-agent

A simple-English summary has not yet been added for this concept.

## Formal definition
A software agent that is used directly by the end-user as the principal. Browsers, email clients, and digital wallets are all examples of user agents.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **user agent** (`en`, `alternative`)
- **user agents** (`en`, `alternative`)

### Related concepts
- [delegation]({{ '/terms/delegation/' | relative_url }})
- [delegator]({{ '/terms/delegator/' | relative_url }})
- [delegatee]({{ '/terms/delegatee/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:delegation`
- **related**: `urn:tig:concept:delegator`
- **related**: `urn:tig:concept:delegatee`
- **related**: `urn:tig:concept:authorization`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:user-agent`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/user-agent.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
user agent, user agents

### Governance profile
- **Authority scope**: delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- delegation_grant

### Assurance
**Evidence artifacts**
- delegation_record

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- delegation_grant

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record

### Notes
Not specified

### Supporting definitions
- [Wikipedia](https://en.wikipedia.org/wiki/User_agent): On the [Web](https://en.wikipedia.org/wiki/World_Wide_Web), a user agent is a [software agent](https://en.wikipedia.org/wiki/Software_agent) capable of and responsible for retrieving and facilitating [end user](https://en.wikipedia.org/wiki/End_user) interaction with Web content.[<sup>\[1\]</sup>](https://en.wikipedia.org/wiki/User_agent#cite_note-1) This includes all common [web browsers](https://en.wikipedia.org/wiki/Web_browser), such as [Google Chrome](https://en.wikipedia.org/wiki/Google_Chrome), [Mozilla Firefox](https://en.wikipedia.org/wiki/Mozilla_Firefox), and [Safari](https://en.wikipedia.org/wiki/Safari_\(web_browser\)), some [email clients](https://en.wikipedia.org/wiki/Email_client), standalone [download managers](https://en.wikipedia.org/wiki/Download_manager) like [youtube-dl](https://en.wikipedia.org/wiki/Youtube-dl), other [command-line](https://en.wikipedia.org/wiki/Command-line) utilities like [cURL](https://en.wikipedia.org/wiki/CURL), and arguably [headless](https://en.wikipedia.org/wiki/Headless_software) [services](https://en.wikipedia.org/wiki/Service_\(systems_architecture\)) that power part of a larger application, such as a [web crawler](https://en.wikipedia.org/wiki/Web_crawler).
- The user agent plays the role of the [client](https://en.wikipedia.org/wiki/Client_\(computing\)) in a [client–server system](https://en.wikipedia.org/wiki/Client%E2%80%93server_model). The [HTTP](https://en.wikipedia.org/wiki/HTTP) [User-Agent header](https://en.wikipedia.org/wiki/User-Agent_header) is intended to clearly identify the agent to the server. However, this header can be omitted or [spoofed](https://en.wikipedia.org/wiki/User_agent_spoofing), so some websites use [other agent detection methods](https://en.wikipedia.org/wiki/Browser_sniffing).

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/user-agent.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
