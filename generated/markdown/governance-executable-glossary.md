# Governance-Executable Glossary

Total terms: **534**

## aal

See: authenticator assurance level.

- Authority scope: access_decisioning, assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## abac

See: attribute-based access control.

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: False

## acceptance-network

A trust network designed to facilitate acceptance of verifiable data for its members.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## acceptance

The action of a party receiving any form of verifiable data and using it to make a trust decision.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## access-control

The process of granting or denying specific requests for obtaining and using information and related information processing services.

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: False

## accreditation

Formal declaration by an accrediting authority that an information system is approved to operate at an acceptable level of risk, based on the implementation of an approved set of technical, managerial, and procedural safeguards.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: True

## acdc

See: Authentic Chained Data Container.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## action

Something that is actually done (a 'unit of work' that is executed) by a single actor (on behalf of a given party), as a single operation, in a specific context.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## actor

An entity that can act (do things/execute actions), e.g. people, machines, but not organizations. A digital agent can serve as an actor acting on behalf of its principal.

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: False

## address

See: network address.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## administering-authority

See: administering body.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: True

## administering-body

A legal entity delegated by a governing body to administer the operation of a governance framework and governed infrastructure for a digital trust ecosystem, such as one or more trust registries.

- Authority scope: policy_definition, delegation_and_scope, governance_recognition
- Delegation mode: direct_or_constrained
- Revocation supported: True

## agency

In the context of decentralized digital trust infrastructure, the empowering of a party to act independently of its own accord, and in particular to empower the party to employ an agent to act on the party's behalf.

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: False

## agent

An actor that executes an action on behalf of a party (called the principal of that actor). In the context of decentralized digital trust infrastructure, the term “agent” is most frequently used to mean a digital agent.

- Authority scope: delegation_and_scope, governance_recognition
- Delegation mode: direct_or_constrained
- Revocation supported: True

## aid

See autonomic-identifier.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## anonymous

An adjective describing when the identity of a natural person or other actor is unknown.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## anycast-address

A network address (especially an IP address used for anycast routing of network transmissions.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## anycast

Anycast is a network addressing and routing methodology in which a single IP-address is shared by devices (generally servers) in multiple locations. Routers direct packets addressed to this destination to the location nearest the sender, using their normal decision-making algorithms, typically the lowest number of BGP network hops. Anycast routing is widely used by content delivery networks such as web and name servers, to bring their content closer to end users.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## appraisability

The ability for a communication endpoint identified with a verifiable identifier (VID) to be appraised for the set of its properties that enable a relying party or a verifier to make a trust decision about communicating with that endpoint.

- Authority scope: verification_and_reliance
- Delegation mode: direct
- Revocation supported: False

## appropriate-friction

A user-experience design principle for information systems (such as digital wallets) specifying that the level of attention required of the holder for a particular transaction should provide a reasonable opportunity for an informed choice by the holder.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## assurance-level

A level of confidence in a claim that may be relied on by others. Different types of assurance levels are defined for different types of trust assurance mechanisms. Examples include authenticator assurance level, federation assurance level, and identity assurance level.

- Authority scope: credential_issuance, access_decisioning, assurance_and_audit
- Delegation mode: direct
- Revocation supported: True

## attestation

The issue of a statement, based on a decision, that fulfillment of specified requirements has been demonstrated. In the context of decentralized digital trust infrastructure, an attestation usually has a digital signature so that it is cryptographically verifiable.

- Authority scope: assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## attribute-based-access-control

An access control approach in which access is mediated based on attributes associated with subjects (requesters) and the objects to be accessed. Each object and subject has a set of associated attributes, such as location, time of creation, access rights, etc. Access to an object is authorized or denied depending upon whether the required (e.g., policy-defined) correlation can be made between the attributes of that object and of the requesting subject.

- Authority scope: policy_definition, access_decisioning
- Delegation mode: direct
- Revocation supported: False

## attribute

An identifiable set of data that describes an entity, which is the subject of the attribute.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## attributional-trust

KERI offers cryptographic root-of-trust to establish attributional trust. In the real world you'd also need reputational-trust. You can't have reputation without attributional trust.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## audit-log

An audit log is a security-relevant chronological record, set of records, and/or destination and source of records that provide documentary evidence of the sequence of activities that have affected at any time a specific operation, procedure, event, or device.

- Authority scope: assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## audit

Independent review and examination of records and activities to assess the adequacy of system controls, to ensure compliance with established policies and operational procedures.

- Authority scope: assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## auditor

The party responsible for performing an audit. Typically an auditor must be accredited.

- Authority scope: assurance_and_audit
- Delegation mode: direct
- Revocation supported: True

## authentic-chained-data-container

A digital data structure designed for both cryptographic verification and chaining of data containers. ACDC may be used for digital credentials.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## authentic-data

integrity and [[xref:toip2, provenance]]'d data.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## authentication

Verifying the identity of a user, process, or device, often as a prerequisite to allowing access to resources in an information system.

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: True

## authenticator-assurance-level

A measure of the strength of an authentication mechanism and, therefore, the confidence in it.

- Authority scope: access_decisioning, assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## authenticator

Something the claimant possesses and controls (typically a cryptographic module or password) that is used to authenticate the claimant’s identity.

- Authority scope: credential_issuance, access_decisioning
- Delegation mode: direct
- Revocation supported: True

## authenticity

The property of being genuine and being able to be verified and trusted; confidence in the validity of a transmission, a message, or message originator.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## authoritative-source

A source of information that a relying party considers to be authoritative for that information. In ToIP architecture, the trust registry authorized by the governance framework for a trust community is typically considered an authoritative source by the members of that trust community. A system of record is an authoritative source for the data records it holds. A trust anchor is an authoritative source for the beginning of a trust chain.

- Authority scope: verification_and_reliance, policy_definition, registry_management, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## authoritative

Information or data that comes from an authority for that information.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: True

## authority

A party whose decisions, policies, rules, or recognition outcomes are accepted as governing, directive, or controlling by other parties within a defined scope.

- Authority scope: policy_definition, delegation_and_scope, governance_recognition
- Delegation mode: direct_or_constrained
- Revocation supported: True

## authorization-graph

A graph of the authorization relationships between different entities in a trust-community. In a digital trust ecosystem, the governing body is typically the trust root of an authorization graph. In some cases, an authorization graph can be traversed by making queries to one or more trust registries.

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: True

## authorization

The process of determining whether a requested action or service is approved for a specific entity under applicable policies, rules, credentials, or other governing criteria.

- Authority scope: credential_issuance, policy_definition, access_decisioning
- Delegation mode: direct
- Revocation supported: True

## authorized-organizational-representative

A person who has the authority to make claims, sign documents or otherwise commit resources on behalf of an organization.

- Authority scope: credential_issuance, delegation_and_scope, governance_recognition
- Delegation mode: direct_or_constrained
- Revocation supported: True

## autonomic-identifier

The specific type of self-certifying identifier defined by the KERI specifications: [[xref:keri1, autonomic-identifier]].

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## autonomic-identity-system

an identity system that includes a primary root-of-trust in self-certifying identifiers that are strongly bound at issuance to a cryptographic signing (public, private) key pair. An AIS enables any entity to establish control over an AN in an independent, interoperable, and portable way.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## autonomic-namespace

a namespace that is self-certifying and hence self-administrating. An AN has a self-certifying prefix that provides cryptographic verification of root control authority over its namespace. All derived AIDs in the same AN share the same root-of-trust, source-of-truth, and locus-of-control (RSL). The governance of the namespace is, therefore, unified into one entity, that is, the controller who is/holds the root authority over the namespace.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: True

## binding

The technique of connecting two data elements together. In the context of key-event-receipt-infrastructure it's the association of data or an identifier with another identifier or a subject (a person, organization or machine), thereby lifting the privacy of the subject through that connection, i.e. **binding**.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## biometric

A measurable physical characteristic or personal behavioral trait used to recognize the AID, or verify the claimed identity, of an applicant. Facial images, fingerprints, and iris scan samples are all examples of biometrics.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: False

## blockchain

A distributed ledger of cryptographically-signed transactions that are grouped into blocks. Each block is cryptographically linked to the previous one (making it tamper evident) after validation and undergoing a consensus decision. As new blocks are added, older blocks become more difficult to modify (creating tamper resistance). New blocks are replicated across copies of the ledger within the network, and any conflicts are resolved automatically using established rules.

- Authority scope: policy_definition
- Delegation mode: direct
- Revocation supported: False

## bola

See broken-object-level-authorization

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: True

## broadcast-address

A broadcast address is a network address used to transmit to all devices connected to a multiple-access communications network. A message sent to a broadcast address may be received by all network-attached hosts. In contrast, a multicast address is used to address a specific group of devices, and a unicast address is used to address a single device. For network layer communications, a broadcast address may be a specific IP address.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## broadcast

In computer networking, telecommunication and information theory, broadcasting is a method of transferring a message to all recipients simultaneously. Broadcast delivers a message to all nodes in the network using a one-to-all association; a single datagram (or packet) from one sender is routed to all of the possibly multiple endpoints associated with the broadcast address. The network automatically replicates datagrams as needed to reach all the recipients within the scope of the broadcast, which is generally an entire network subnet.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## broken-object-level-authorization

Refers to security flaws where users can access data they shouldn't, due to inadequate permission checks on individual (sub)objects.

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: True

## c2pa

See: Coalition for Content Provenance and Authenticity.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## ca

See: certificate authority.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: True

## cai

See: Content Authenticity Initiative.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## capability

The ability or permission for an actor or agent to perform a specific action on behalf of a party within a defined scope and subject to applicable constraints.

- Authority scope: delegation_and_scope, access_decisioning
- Delegation mode: direct_or_constrained
- Revocation supported: True

## certificate-authority

The entity in a public key infrastructure (PKI) that is responsible for issuing public key certificates and exacting compliance to a PKI policy.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## certificate

See: public key certificate.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## certification-authority

See: certificate authority.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: True

## certification-body

A legal entity that performs certification.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## certification

A comprehensive assessment of the management, operational, and technical security controls in an information system, made in support of security accreditation, to determine the extent to which the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting the security requirements for the system.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: False

## chain-of-trust

See: trust chain.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## chained-credentials

Two or more credentials linked together to create a trust chain between the credentials that is cryptographically verifiable.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## chaining

See: trust chain.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## channel

See: communication channel.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## ciphertext

Encrypted (enciphered) data. The confidential form of the plaintext that is the output of the encryption function.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## claim

An assertion about a subject, typically expressed as an attribute or property of the subject. It is called a “claim” because the assertion is always made by some party, called the issuer of the claim, and the validity of the claim must be judged by the verifier.

- Authority scope: credential_issuance, verification_and_reliance
- Delegation mode: direct
- Revocation supported: False

## coalition-for-content-provenance-and-authenticity

C2PA is a Joint Development Foundation project of the Linux Foundation that addresses the prevalence of misleading information online through the development of technical standards for certifying the source and history (or provenance) of media content.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## collective-signature

a group signature scheme, that (i) is shared by a set of signing groups and (ii) combined collective signature shared by several signing groups and several individual signers. The protocol of the first type is constructed and described in detail. It is possible to modify the described protocol which allows transforming the protocol of the first type into the protocol of the second type. The proposed collective signature protocols have significant merits, one of which is connected with possibility of their practical using on the base of the existing public key infrastructures.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## communication-channel

A communication channel refers either to a physical transmission medium such as a wire, or to a logical connection over a multiplexed medium such as a radio channel in telecommunications and computer networking. A channel is used for information transfer of, for example, a digital bit stream, from one or several senders to one or several receivers.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## communication-endpoint

A type of communication network node. It is an interface exposed by a communicating party or by a communication channel. An example of the latter type of a communication endpoint is a publish-subscribe topic or a group in group communication systems.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## communication-metadata

Metadata that describes the sender, receiver, routing, handling, or contents of a communication. Communication metadata is often observable even if the contents of the communication are encrypted.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## communication-session

A finite period for which a communication channel is instantiated and maintained, during which certain properties of that channel, such as authentication of the participants, are in effect. A session has a beginning, called the session initiation, and an ending, called the session termination.

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: False

## communication

The transmission of information.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## complex-password

A password that meets certain security requirements, such as minimum length, inclusion of different character types, non-repetition of characters, and so on.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## compliance

In the context of decentralized digital trust infrastructure, compliance is the extent to which a system, actor, or party conforms to the requirements of a regulation, governance framework, or trust framework that pertains to that particular entity.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## concept

An abstract idea that enables the classification of entities, i.e., a mental construct that enables an instance of a class of entities to be distinguished from entities that are not an instance of that class. A concept can be identified with a term.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## confidential-computing

Hardware-enabled features that isolate and process encrypted data in memory so that the data is at less risk of exposure and compromise from concurrent workloads or the underlying system and platform.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## confidentiality

In a communications context, a type of privacy protection in which messages use encryption or other privacy-preserving technologies so that only authorized parties have access.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## connection

A communication channel established between two communication endpoints. A connection may be ephemeral or persistent.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## consent-management

A system, process or set of policies under which a person agrees to share personal data for specific usages. A consent management system will typically create a record of such consent.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## content-authenticity-initiative

The Content Authenticity Initiative (CAI) is an association founded in November 2019 by Adobe, the New York Times and Twitter. The CAI promotes an industry standard for provenance metadata defined by the C2PA. The CAI cites curbing disinformation as one motivation for its activities.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## contextual-linkability

Refers to the condition where vendors or other data capture points provide enough context at point of capture to be able to use statistical correlation with existing data sets to link any of a person's disclosed attributes to a set of already known data points about a given person.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## control-authority

In identity systems, control authority is the power to determine who controls what. It is a primary factor in determining the basis for trust in those systems.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: True

## controlled-document

A governance document whose authority is derived from a primary document.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: True

## controller

In the context of digital communications, the entity in control of sending and receiving digital communications. In the context of decentralized digital trust infrastructure, the entity in control of the cryptographic keys necessary to perform cryptographically verifiable actions using a digital agent and digital wallet. In a ToIP context, the entity in control of a ToIP endpoint.

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: False

## correlation-privacy

In a communications context, a type of privacy protection in which messages use encryption, hashes, or other privacy-preserving technologies to avoid the use of identifiers or other content that unauthorized parties may use to correlate the sender and/or receiver(s).

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## counterparty

From the perspective of one party, the other party in a transaction, such as a financial transaction.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## credential-family

A set of related digital credentials defined by a governing body (typically in a governance framework) to empower transitive trust decisions among the participants in a digital trust ecosystem.

- Authority scope: credential_issuance, policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## credential-governance-framework

A governance framework for a credential family. A credential governance framework may be included within or referenced by an ecosystem governance framework.

- Authority scope: credential_issuance, policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## credential-offer

A protocol request invoked by an issuer to offer to issue a digital credential to the  holder of a digital wallet. If the request is invoked by the holder, it is called an issuance request.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## credential-request

See: issuance request.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## credential-schema

A data schema describing the structure of a digital credential. The W3C Verifiable Credentials Data Model Specification defines a set of requirements for credential schemas.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## credential

A container of claims describing one or more subjects. A credential is generated by the issuer of the credential and given to the holder of the credential. A credential typically includes a signature or some other means of proving its authenticity. A credential may be either a physical credential or a digital credential.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## criterion

In the context of terminology, a written description of a concept that anyone can evaluate to determine whether or not an entity is an instance or example of that concept. Evaluation leads to a yes/no result.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## cryptographic-binding

Associating two or more related elements of information using cryptographic techniques.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## cryptographic-key

A key in cryptography is a piece of information, usually a string of numbers or letters that are stored in a file, which, when processed through a cryptographic algorithm, can encode or decode cryptographic data. Symmetric cryptography refers to the practice of the same key being used for both encryption and decryption. Asymmetric cryptography has separate keys for encrypting and decrypting. These keys are known as the public keys and private keys, respectively.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## cryptographic-trust

A specialized type of technical trust that is achieved using cryptographic algorithms.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## cryptographic-verifiability

The property of being cryptographically verifiable.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## cryptographically-bound

A state in which two or more elements of information have a cryptographic binding.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## cryptographically-verifiable

A property of a data structure that has been digitally signed using a private key such that the digital signature can be verified using the public key. Verifiable data, verifiable messages, verifiable credentials, and verifiable data registries are all cryptographically verifiable. Cryptographic verifiability is a primary goal of the ToIP Technology Stack.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## cryptography

TODO

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## custodial-wallet

A digital wallet that is directly in the custody of a principal, i.e., under the principal’s direct personal or organizational control. A digital wallet that is in the custody of a third party is called a non-custodial wallet.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## custodian

A third party that has been assigned rights and duties in a custodianship arrangement for the purpose of hosting and safeguarding a principal's private keys, digital wallet and digital assets on the principal’s behalf. Depending on the custodianship arrangement, the custodian may act as an exchange and provide additional services, such as staking, lending, account recovery, or security features.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## custodianship-arrangement

The informal terms or formal legal agreement under which a custodian agrees to provide service to a principal.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## dark-pattern

A design pattern, mainly in user interfaces, that has the effect of deceiving individuals into making choices that are advantageous to the designer.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## data-packet

In telecommunications and computer networking, a network packet is a formatted unit of data carried by a packet-switched network such as the Internet. A packet consists of control information and user data; the latter is also known as the payload. Control information provides data for delivering the payload (e.g., source and destination network addresses, error detection codes, or sequencing information). Typically, control information is found in packet headers and trailers.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## data-schema

A description of the structure of a digital document or object, typically expressed in a machine-readable language in terms of constraints on the structure and content of documents or objects of that type. A credential schema is a particular type of data schema.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## data-subject

The natural person that is described by personal data. Data subject is the term used by the EU General Data Protection Regulation.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## data-vault

See: digital vault.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## data

In the pursuit of knowledge, data is a collection of discrete values that convey information, describing quantity, quality, fact, statistics, other basic units of meaning, or simply sequences of symbols that may be further interpreted. A datum is an individual value in a collection of data.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## datagram

See: data packet.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## dead-drop

In cybersecurity or digital privacy scenarios, the term "dead drop" refers to encrypted or secure virtual spaces where information can be deposited or retrieved anonymously. In the credentials field, the presenter controls the disclosure, so you can't re-identify the data.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## decentralized-identifier

A globally unique persistent identifier that does not require a centralized registration authority and is often generated and/or registered cryptographically. The generic format of a DID is defined in section 3.1 DID Syntax of the W3C Decentralized Identifiers (DIDs) 1.0 specification. A specific DID scheme is defined in a DID method specification.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: True

## decentralized-identity-foundation

A non-profit project of the Linux Foundation chartered to develop the foundational components of an open, standards-based, decentralized identity ecosystem for people, organizations, apps, and devices.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## decentralized-identity

A digital identity architecture in which a digital identity is established via the control of a set of cryptographic keys in a digital wallet so that the controller is not dependent on any external identity provider or other third party.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## decentralized-web-node

A decentralized personal and application data storage and message relay node, as defined in the DIF Decentralized Web Node specification. Users may have multiple nodes that replicate their data between them.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## deceptive-pattern

See: dark pattern.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## decryption

The process of changing ciphertext into plaintext using a cryptographic algorithm and key. The opposite of encryption.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## deep-link

In the context of the World Wide Web, deep linking is the use of a hyperlink that links to a specific, generally searchable or indexed, piece of web content on a website (e.g. "https\://example.com/path/page"), rather than the website's home page (e.g., "https\://example.com"). The URL contains all the information needed to point to a particular item. Deep linking is different from mobile deep linking, which refers to directly linking to in-app content using a non-HTTP URI.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## definition

A textual statement defining the meaning of a term by specifying criterion that enable the concept identified by the term to be distinguished from all other concepts within the intended scope.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## delegatee

The second party receiving a delegation from a first party (the delegator) and authorized to act only within the granted scope and applicable constraints.

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: True

## delegation-credential

A credential used to perform delegation.

- Authority scope: credential_issuance, delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: True

## delegation

The act of a first party (the delegator) authorizing a second party (the delegatee) to perform a defined set of actions on behalf of the first party within an authorized scope and subject to applicable constraints.

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: True

## delegator

The first party that makes a delegation to a second party (the delegatee) and remains accountable for granting authority within the permitted scope.

- Authority scope: delegation_and_scope, governance_recognition
- Delegation mode: direct_or_constrained
- Revocation supported: True

## dependent

An entity for the caring for and/or protecting/guarding/defending of which a guardianship arrangement has been established with a guardian.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## device-controller

The controller of a device capable of digital communications, e.g., a smartphone, tablet, laptop, IoT device, etc.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## dictionary

A dictionary is a listing of lexemes (words or terms) from the lexicon of one or more specific languages, often arranged alphabetically, which may include information on definitions, usage, etymologies, pronunciations, translation, etc. It is a lexicographical reference that shows inter-relationships among the data. Unlike a glossary, a dictionary may provide multiple definitions of a term depending on its scope or context.

- Authority scope: registry_management
- Delegation mode: direct
- Revocation supported: False

## did-controller

An entity that has the capability to make changes to a DID document. A DID might have more than one DID controller. The DID controller(s) can be denoted by the optional `controller` property at the top level of the DID document. Note that a DID controller might be the DID subject.

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: False

## did-document

A set of data describing the DID subject, including mechanisms, such as cryptographic public keys, that the DID subject or a DID delegate can use to authenticate itself and prove its association with the DID. A DID document might have one or more different representations as defined in section 6 of the W3C Decentralized Identifiers (DIDs) 1.0 specification.

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: True

## did-method

A definition of how a specific DID method scheme is implemented. A DID method is defined by a DID method specification, which specifies the precise operations by which DIDs and DID documents are created, resolved, updated, and deactivated.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## did-subject

The entity identified by a DID and described by a DID document. Anything can be a DID subject: person, group, organization, physical thing, digital thing, logical thing, etc.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## did-url

A DID plus any additional syntactic component that conforms to the definition in section 3.2 of the W3C Decentralized Identifiers (DIDs) 1.0 specification. This includes an optional DID path (with its leading / character), optional DID query (with its leading ? character), and optional DID fragment (with its leading # character).

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## did

See: decentralized identifier

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## digital-agent

In the context of ​​decentralized digital trust infrastructure, a software agent that operates in conjunction with a digital wallet or similar system component to take actions on behalf of its controller.

- Authority scope: delegation_and_scope, governance_recognition
- Delegation mode: direct_or_constrained
- Revocation supported: True

## digital-asset

A digital asset is anything that exists only in digital form and comes with a distinct usage right. Data that do not possess that right are not considered assets.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## digital-certificate

See: public key certificate.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## digital-credential

A credential in digital form that is signed with a digital signature and held in a digital wallet. A digital credential is issued to a holder by an issuer; a proof of the credential is presented by the holder to a verifier.

- Authority scope: credential_issuance, verification_and_reliance
- Delegation mode: direct
- Revocation supported: True

## digital-ecosystem

A digital ecosystem is a distributed, adaptive, open socio-technical system with properties of self-organization, scalability and sustainability inspired from natural ecosystems. Digital ecosystem models are informed by knowledge of natural ecosystems, especially for aspects related to competition and collaboration among diverse entities.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## digital-identity

An identity expressed in a digital form for the purpose representing the identified entity within a computer system or digital network.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## digital-rights-management

Digital rights management (DRM) is the management of legal access to digital content. Various tools or technological protection measures (TPM) like access control technologies, can restrict the use of proprietary hardware and copyrighted works. DRM technologies govern the use, modification and distribution of copyrighted works (e.g. software, multimedia content) and of systems that enforce these policies within devices.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## digital-signature

A digital signature is a mathematical scheme that uses cryptography for verifying the authenticity of digital messages or documents. A valid digital signature, where the prerequisites are satisfied, gives a recipient very high confidence that the message was created by a known sender (authenticity), and that the message was not altered in transit (integrity).

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## digital-trust-ecosystem

A digital ecosystem in which the participants are one or more interoperating trust communities. Governance of the various roles of governed parties within a digital trust ecosystem (e.g., issuers, holders, verifiers, certification bodies, auditors) is typically managed by a governing body using a governance framework as recommended in the ToIP Governance Stack. Many digital trust ecosystems will also maintain one or more trust lists and/or trust registries.

- Authority scope: credential_issuance, verification_and_reliance, policy_definition, registry_management, assurance_and_audit, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## digital-trust-utility

An information system, network, distributed database, or blockchain designed to provide one or more supporting services to higher level components of decentralized digital trust infrastructure. In the ToIP stack, digital trust utilities are at Layer 1. A verifiable data registry is one type of digital trust utility.

- Authority scope: registry_management
- Delegation mode: direct
- Revocation supported: True

## digital-vault

A secure container for data whose controller is the principal. A digital vault is most commonly used in conjunction with a digital wallet and a digital agent. A digital vault may be implemented on a local device or in the cloud; multiple digital vaults may be used by the same principal across different devices and/or the cloud; if so they may use some type of synchronization. If the capability is supported, data may flow into or out of the digital vault automatically based on subscriptions approved by the controller.

- Authority scope: delegation_and_scope, access_decisioning
- Delegation mode: direct_or_constrained
- Revocation supported: False

## digital-wallet

A user agent, optionally including a hardware component, capable of securely storing and processing cryptographic keys, digital credentials, digital assets and other sensitive private data that enables the controller to perform cryptographically verifiable operations. A non-custodial wallet is directly in the custody of a principal. A custodial wallet is in the custody of a third party. Personal wallets are held by individual persons; enterprise wallets are held by organizations or other legal entities.

- Authority scope: credential_issuance, verification_and_reliance, delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: True

## discovery

A mechanism that helps systems or devices find each other automatically, often used in networks to identify services or resources. In decentralized identifier systems it helps to locate and verify digital identities without relying on a central authority.

- Authority scope: verification_and_reliance, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## distributed-ledger

A distributed ledger (also called a shared ledger or distributed ledger technology or DLT) is the consensus of replicated, shared, and synchronized digital data that is geographically spread (distributed) across many sites, countries, or institutions. In contrast to a centralized database, a distributed ledger does not require a central administrator, and consequently does not have a single (central) point-of-failure. In general, a distributed ledger requires a peer-to-peer (P2P) computer network and consensus algorithms so that the ledger is reliably replicated across distributed computer nodes (servers, clients, etc.). The most common form of distributed ledger technology is the blockchain, which can either be on a public or private network.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## domain

See: security domain.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## drm

See: digital rights management.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## dwn

See: Decentralized Web Node.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## ecosystem-governance-framework

A governance framework for a digital trust ecosystem. An ecosystem governance framework may incorporate, aggregate, or reference other types of governance frameworks such as a credential governance framework or a utility governance framework.

- Authority scope: credential_issuance, policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## ecosystem

See: digital ecosystem.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## eidas

eIDAS (electronic IDentification, Authentication and trust Services) is an EU regulation with the stated purpose of governing "electronic identification and trust services for electronic transactions". It passed in 2014 and its provisions came into effect between 2016-2018.

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: False

## encrypt-sender-sign-receiver

An authenticated encryption approach, using PKI. It covers authenticity and confidentiality.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## encrypted-data-vault

See: digital vault.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## encryption

Cryptographic transformation of data (called plaintext) into a form (called ciphertext) that conceals the data's original meaning to prevent it from being known or used. If the transformation is reversible, the corresponding reversal process is called decryption, which is a transformation that restores encrypted data to its original state.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## end-to-end-encryption

Encryption that is applied to a communication before it is transmitted from the sender’s communication endpoint and cannot be decrypted until after it is received at the receiver’s communication endpoint. When end-to-end encryption is used, the communication cannot be decrypted in transit no matter how many intermediaries are involved in the routing process.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## end-to-end-principle

The end-to-end principle is a design framework in computer networking. In networks designed according to this principle, guaranteeing certain application-specific features, such as reliability and security, requires that they reside in the communicating end nodes of the network. Intermediary nodes, such as gateways and routers, that exist to establish the network, may implement these to improve efficiency but cannot guarantee end-to-end correctness.

- Authority scope: policy_definition
- Delegation mode: direct
- Revocation supported: False

## end-verifiability

a data item or statement may be cryptographically securely attributable to its source (party at the source end) by any recipient verifier (party at the destination end) without reliance on any infrastructure not under the verifier’s ultimate control.

- Authority scope: verification_and_reliance
- Delegation mode: direct
- Revocation supported: False

## end-verifiable

When a log is _end verifiable_, it means that the log may be verified by any end user that receives a copy. No trust in intervening infrastructure is needed to verify the log and validate the content.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## endpoint-system

The system that operates a communications endpoint. In the context of the ToIP stack, an endpoint system is one of three types of systems defined in the ToIP Technology Architecture Specification.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## endpoint

See: communication endpoint.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## enterprise-data-vault

A digital vault whose controller is an organization.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## enterprise-wallet

A digital wallet whose holder is an organization.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## entity

Someone or something that is known to exist.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## ephemeral-connection

A connection that only exists for the duration of a single communication session or transaction.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## essr

Encrypt‐Sender‐Sign‐Receiver

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## expression-language

A language for creating a computer-interpretable (machine-readable) representation of specific knowledge.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## fal

See: federation assurance level.

- Authority scope: assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## federated-identity

A digital identity architecture in which a digital identity established on one computer system, network, or trust domain is linked to other computer systems, networks, or trust domains for the purpose of identifying the same entity across those domains.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## federation-assurance-level

A category that describes the federation protocol used to communicate an assertion containing authentication) and attribute information (if applicable) to a relying party, as defined in NIST SP 800-63-3 in terms of three levels: FAL 1 (Some confidence), FAL 2 (High confidence), FAL 3 (Very high confidence).

- Authority scope: verification_and_reliance, access_decisioning, assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## federation

A group of organizations that collaborate to establish a common trust framework or governance framework for the exchange of identity data in a federated identity system.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## fiduciary

A fiduciary is a person who holds a legal or ethical relationship of trust with one or more other parties (person or group of persons). Typically, a fiduciary prudently takes care of money or other assets for another person. One party, for example, a corporate trust company or the trust department of a bank, acts in a fiduciary capacity to another party, who, for example, has entrusted funds to the fiduciary for safekeeping or investment. In a fiduciary relationship, one person, in a position of vulnerability, justifiably vests confidence, good faith, reliance, and trust in another whose aid, advice, or protection is sought in some matter.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## first-party

The party who initiates a trust relationship, connection, or transaction with a second party.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## foundational-identity

A set of identity data, such as a credential, issued by an authoritative source for the legal identity of the subject. Birth certificates, passports, driving licenses, and other forms of government ID documents are considered foundational identity documents. Foundational identities are often used to provide identity binding for functional identities.

- Authority scope: credential_issuance, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## fourth-party

A party that is not directly involved in the trust relationship between a first party and a second party, but provides supporting services exclusively to the first party (in contrast with a third party, who in most cases provides supporting services to the second party). In its strongest form, a fourth party has a fiduciary relationship with the first party.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## functional-identity

A set of identity data, such as a credential, that is issued not for the purpose of establishing a foundational identity for the subject, but for the purpose of establishing other attributes, qualifications, or capabilities of the subject. Loyalty cards, library cards, and employee IDs are all examples of functional identities. Foundational identities are often used to provide identity binding for functional identities.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## gateway

A gateway is a piece of networking hardware or software used in telecommunications networks that allows data to flow from one discrete network to another. Gateways are distinct from routers or switches in that they communicate using more than one protocol to connect multiple networks<sup>\[1\]\[2\]</sup>#cite_note-1) and can operate at any of the seven layers of the open systems interconnection model (OSI).

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## gdpr

See: General Data Protection Regulation.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## general-data-protection-regulation

The General Data Protection Regulation (Regulation (EU) 2016/679, abbreviated GDPR) is a European Union regulation on information privacy in the European Union (EU) and the European Economic Area (EEA). The GDPR is an important component of EU privacy law and human rights law, in particular Article 8(1) of the Charter of Fundamental Rights of the European Union. It also governs the transfer of personal data outside the EU and EEA. The GDPR's goals are to enhance individuals' control and rights over their personal information and to simplify the regulations for international business.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## glossary

A glossary (from Ancient Greek: γλῶσσα, glossa; language, speech, wording), also known as a _vocabulary_ or _clavis_, is an alphabetical list of terms in a particular domain of knowledge (scope) together with the definitions for those terms. Unlike a dictionary, a glossary has only one definition for each term.

- Authority scope: registry_management
- Delegation mode: direct
- Revocation supported: False

## governance-diamond

A term that refers to the addition of a governing body to the standard trust triangle of issuers, holders, and verifiers of credentials. The resulting combination of four parties represents the basic structure of a digital trust ecosystem.

- Authority scope: credential_issuance, verification_and_reliance, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## governance-document

A document with at least one identifier that specifies governance requirements for a trust community.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## governance-framework

A collection of one or more governance documents published by the governing body of a trust community that defines the rules, roles, responsibilities, and decision rights under which that community operates.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## governance-graph

A graph of the governance relationships between entities with a trust community. A governance graph shows which nodes are the governing bodies and which are the governed parties. In some cases, a governance graph can be traversed by making queries to one or more trust registries.Note: a party can play both roles and also be a participant in multiple governance frameworks.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## governance-requirement

A requirement such as a policy, rule, or technical specification specified in a governance document.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## governance-risk-management-compliance

Governance, risk management, and compliance (GRC) are three related facets that aim to assure an organization reliably achieves objectives, addresses uncertainty and acts with integrity. Governance is the combination of processes established and executed by the directors (or the board of directors) that are reflected in the organization's structure and how it is managed and led toward achieving goals. Risk management is predicting and managing risks that could hinder the organization from reliably achieving its objectives under uncertainty. Compliance refers to adhering with the mandated boundaries (laws and regulations) and voluntary boundaries (company's policies, procedures, etc.)

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: False

## governance

The act or process of governing or overseeing the realization of (the results associated with) a set of objectives by the owner of these objectives, in order to ensure they will be fit for the purposes that this owner intends to use them for.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: False

## governed-information

Any information published under the authority of a governing body for the purpose of governing a trust community. This includes its governance framework and any information available via an authorized trust registry.

- Authority scope: policy_definition, registry_management, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## governed-party

A party whose role(s) in a trust community is governed by the governance requirements in a governance framework.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## governed-use-case

A use case specified in a governance document that results in specific governance requirements within that governance framework. Governed use cases may optionally be discovered via a trust registry authorized by the relevant governance framework.

- Authority scope: policy_definition, registry_management, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## governing-authority

See: governing body.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: True

## governing-body

The party (or set of parties) authoritative for governing a trust community, usually (but not always) by developing, publishing, maintaining, and enforcing a governance framework. A governing body may be a government, a formal legal entity of any kind, an informal group of any kind, or an individual. A governing body may also delegate operational responsibilities to an administering body.

- Authority scope: policy_definition, delegation_and_scope, governance_recognition
- Delegation mode: direct_or_constrained
- Revocation supported: True

## grc

See: Governance - Risk Management - Compliance.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: False

## guardian

A party that has been assigned rights and duties in a guardianship arrangement for the purpose of caring for, protecting, guarding, and defending the entity that is the dependent in that guardianship arrangement. In the context of decentralized digital trust infrastructure, a guardian is issued guardianship credentials into their own digital wallet in order to perform such actions on behalf of the dependent as are required by this role.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## guardianship-arrangement

A guardianship arrangement (in a jurisdiction) is the specification of a set of rights and duties between legal entities of the [[ref: jurisdiction] that enforces these rights and duties, for the purpose of caring for, protecting, guarding, and defending one or more of these [[erf: entities]]. At a minimum, the entities participating in a guardianship arrangement are the guardian and the dependent.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## guardianship-credential

A digital credential issued by a governing body to a guardian to empower the guardian to undertake the rights and duties of a guardianship arrangement on behalf of a dependent.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## hardware-security-module

A physical computing device that provides tamper-evident and intrusion-resistant safeguarding and management of digital keys and other secrets, as well as crypto-processing.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## hash-function

An algorithm that computes a numerical value (called the hash value) on a data file or electronic message that is used to represent that file or message, and depends on the entire contents of the file or message. A hash function can be considered to be a fingerprint of the file or message. Approved hash functions satisfy the following properties: _one-way_ (it is computationally infeasible to find any input that maps to any pre-specified output); and _collision resistant_ (it is computationally infeasible to find any two distinct inputs that map to the same output).

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## hash

The result of applying a hash function to a message.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## holder-binding

The process of creating and verifying a relationship between the holder of a digital wallet and the wallet itself. Holder binding is related to but NOT the same as subject binding.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## holder

A role an agent performs by serving as the controller of the cryptographic keys and digital credentials in a digital wallet. The holder makes issuance requests for credentials and responds to presentation requests for credentials. A holder is usually, but not always, a subject of the credentials they are holding.

- Authority scope: credential_issuance, delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: True

## host

A host is any hardware device that has the capability of permitting access to a network via a user interface, specialized software, network address, protocol stack, or any other means. Some examples include, but are not limited to, computers, personal electronic devices, thin clients, and multi-functional devices.

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: False

## hourglass-model

An architectural model for layered systems—and specifically for the protocol layers in a protocol stack—in which a diversity of supporting protocols and services at the lower layers are able to support a great diversity of protocols and applications at the higher layers through the use of a single protocol in the spanning layer in the middle—the “neck” of the hourglass.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## hsm

See: hardware security module.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## human-auditable

A process or procedure whose compliance with the policies in a trust framework or governance framework can only be verified by a human performing an audit. Human auditability is a primary goal of the ToIP Governance Stack.

- Authority scope: policy_definition, assurance_and_audit, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## human-experience

The processes, patterns and rituals of acquiring knowledge or skill from doing, seeing, or feeling things as a natural person. In the context of decentralized digital trust infrastructure, the direct experience of a natural person using trust applications to make trust decisions within one or more digital trust ecosystems.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## human-readable

Information that can be processed by a human but that is not intended to be machine-readable.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## human-trust

A level of assurance in a trust relationship or a trust decision that can be achieved only via human evaluation of applicable trust factors.

- Authority scope: assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## ial

See: identity assurance level.

- Authority scope: assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## identification

The action of a party obtaining the set of identity data necessary to serve as that party’s identity for a specific entity.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## identifier

A single attribute—typically a character string—that uniquely identifies an entity within a specific context (which may be a global context). Examples include the name of a party, the URL of an organization, or a serial number for a man-made thing.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## identity-assurance-level

A category that conveys the degree of confidence that a person’s claimed identity is their real identity, for example as defined in NIST SP 800-63-3 in terms of three levels: IAL 1 (Some confidence), IAL 2 (High confidence), IAL 3 (Very high confidence).

- Authority scope: credential_issuance, assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## identity-assurance

The heavy-lifting to be done by a trusted (middle-man) party to establish - and then offer reputational trust. An example of such a party is [[xref:keri1, GLEIF]]. Instead, KERI is for attributional-trust. In the real world you need both.

- Authority scope: assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## identity-binding

The process of associating a set of identity data, such as a credential, with its subject, such as a natural person. The strength of an identity binding is one factor in determining an authenticator assurance level.

- Authority scope: credential_issuance, access_decisioning, assurance_and_audit
- Delegation mode: direct
- Revocation supported: True

## identity-controller

The controller (e.g., a natural person or organization) of an identity, especially a digital identity.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## identity-data

The set of data held by a party in order to provide an identity for a specific entity.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## identity-document

A physical or digital document containing identity data. A credential is a specialized form of identity document. Birth certificates, bank statements, and utility bills can all be considered identity documents.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## identity-proofing

The process of a party gathering sufficient identity data to establish an identity for a particular subject at a particular identity assurance level.

- Authority scope: assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## identity-provider

An identity provider (abbreviated IdP or IDP) is a system entity that creates, maintains, and manages identity information for principals and also provides authentication services to relying applications within a federation or distributed network.

- Authority scope: verification_and_reliance, access_decisioning
- Delegation mode: direct
- Revocation supported: False

## identity

A collection of attributes or other identity data that describe an entity and enable it to be distinguished from all other entities within a specific scope of identification. Identity attributes may include one or more identifiers for an entity, however it is possible to establish an identity without using identifiers.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## idp

See: identity provider.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## impersonation

In the context of cybersecurity, impersonation is when an attacker pretends to be another person in order to commit fraud or some other digital crime.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## information-theoretic-security

the highest level of cryptographic security concerning a cryptographic secret (seed, salt, or private key).

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## integrity

- General IT: [[xref:toip2, integrity]] and KERI specific: [[xref:keri1, integrity]]

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## intermediary-system

An intermediary system routes messages between endpoint systems but is not otherwise involved in the processing of those messages. In the context of end-to-end encryption, intermediary systems cannot decrypt the messages sent between the endpoint systems. In the ToIP stack, intermediary systems operate at ToIP Layer 2, the trust spanning layer. An intermediary system is one of three types of systems defined in the ToIP Technology Architecture Specification; the other two are endpoint systems and supporting systems.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## internet-protocol-suite

The Internet protocol suite, commonly known as TCP/IP, is a framework for organizing the set of communication protocols used in the Internet and similar computer networks according to functional criteria. The foundational protocols in the suite are the Transmission Control Protocol (TCP), the User Datagram Protocol (UDP), and the Internet Protocol (IP).

- Authority scope: policy_definition
- Delegation mode: direct
- Revocation supported: False

## internet-protocol

The Internet Protocol (IP) is the network layer communications protocol in the Internet protocol suite (also known as the TCP/IP suite) for relaying datagrams across network boundaries. Its routing function enables internetworking, and essentially establishes the Internet. IP has the task of delivering packets from the source host to the destination host solely based on the IP addresses in the packet headers. For this purpose, IP defines packet structures that encapsulate the data to be delivered. It also defines addressing methods that are used to label the datagram with source and destination information.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## ip-address

An Internet Protocol address (IP address) is a numerical label such as 192.0.2.1 that is connected to a computer network that uses the Internet Protocol for communication. An IP address serves two main functions: network interface identification, and location addressing.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## ip

See: Internet Protocol.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## issuance-request

A protocol request invoked by the holder of a digital wallet to obtain a digital credential from an issuer.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## issuance

The action of an issuer producing and transmitting a digital credential to a holder. A holder may request issuance by submitting an issuance request.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## issuer

A role an agent performs to assert a set of claims, package and digitally sign them, typically in the form of a digital credential, and transmit them to a holder under applicable policy and governance constraints.

- Authority scope: credential_issuance, policy_definition, delegation_and_scope, governance_recognition
- Delegation mode: direct_or_constrained
- Revocation supported: True

## itps

information-theoretic-security

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## jurisdiction

The composition of: a) a legal system (legislation, enforcement thereof, and conflict resolution), b) a party that governs that legal system, c) a scope within which that legal system is operational, and d) one or more objectives for the purpose of which the legal system is operated.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## kate

See: keys-at-the-edge.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## keri

See: Key Event Receipt Infrastructure.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## key-establishment

A process that results in the sharing of a key between two or more entities, either by transporting a key from one entity to another (key transport) or generating a key from information shared by the entities (key agreement).

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## key-event-log

An ordered sequence of records of key events.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## key-event-receipt-infrastructure

A decentralized permissionless key management architecture.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## key-event

An event in the history of the usage of a cryptographic key pair. There are multiple types of key events. The inception event is when the key pair is first generated. A rotation event is when the key pair is changed to a new key pair. In some key management systems (such as KERI), key events are tracked in a key event log.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## key-management-system

A system for the management of cryptographic keys and their metadata (e.g., generation, distribution, storage, backup, archive, recovery, use, revocation, and destruction). An automated key management system may be used to oversee, automate, and secure the key management process. A key management is often protected by implementing it within the trusted execution environment (TEE) of a device. An example is the Secure Enclave on Apple iOS devices.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## key

See: cryptographic key.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## keys-at-the-edge

A key management architecture in which keys are stored on a user’s local edge devices, such as a smartphone, tablet, or laptop, and then used in conjunction with a secure protocol to unlock a key management system (KMS) and/or a digital vault in the cloud. This approach can enable the storage and sharing of large data structures that are not feasible on edge devices. This architecture can also be used in conjunction with confidential computing to enable cloud-based digital agents to safely carry out “user not present” operations.

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: False

## kms

See: key management system.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## knowledge

The (intangible) sum of what is known by a specific party, as well as the familiarity, awareness or understanding of someone or something by that party.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## laws-of-identity

A set of seven “laws” written by Kim Cameron, former Chief Identity Architect of Microsoft (1941-2021), to describe the dynamics that cause digital identity systems to succeed or fail in various contexts. His goal was to define the requirements for a unifying identity metasystem that can offer the Internet the identity layer it needs.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## layer-1

See: ToIP Layer 1.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## layer-2

See: ToIP Layer 2.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## layer-3

See: ToIP Layer 3.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## layer-4

See: ToIP Layer 4.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## legal-entity-identifier

The Legal Entity Identifier (LEI) is a unique global identifier for legal entities participating in financial transactions. Also known as an LEI code or LEI number, its purpose is to help identify legal entities on a globally accessible database. Legal entities are organisations such as companies or government entities that participate in financial transactions.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## legal-entity

An entity that is not a natural person but is recognized as having legal rights and responsibilities. Examples include corporations, partnerships, sole proprietorships, non-profit organizations, associations, and governments. (In some cases even natural systems such as rivers are treated as legal entities.)

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## legal-identity

A set of identity data considered authoritative to identify a party for purposes of legal accountability under one or more jurisdictions.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: False

## legal-person

In law, a legal person is any person or 'thing' that can do the things a human person is usually able to do in law – such as enter into contracts, sue and be sued, own property, and so on.<sup>\[3\]\[4\]\[5\]</sup> The reason for the term "legal person" is that some legal persons are not people: companies and corporations are "persons" legally speaking (they can legally do most of the things an ordinary person can do), but they are not people in a literal sense (human beings).

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## legal-system

A system in which policies and rules are defined, and mechanisms for their enforcement and conflict resolution are (implicitly or explicitly) specified. Legal systems are not just defined by governments; they can also be defined by a governance framework.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## legitimized-human-meaningful-identifier

An AID and its associated self-certifying trust basis gives rise to a trust domain for associated cryptographically verifiable non-repudiable statements. Every other type of identifier including human meaningful identifiers may then be secured in this resultant trust domain via an end-verifiable authorization. This authorization legitimizes that human meaningful identifier as an LID through its association with an AID. The result is a secured trust domain specific identifier couplet of aid|lid.

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: True

## lei

See: Legal Entity Identifier.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## level-of-assurance

See: assurance level.

- Authority scope: assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## lid

legitimized-human-meaningful-identifier

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## liveness-detection

Any technique used to detect a presentation attack by determining whether the source of a biometric sample is a live human being or a fake representation. This is typically accomplished using algorithms that analyze biometric sensor data to detect whether the source is live or reproduced.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## locus-of-control

The set of computing systems under a party’s direct control, where messages and data do not cross trust boundaries.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## machine-readable

Information written in a computer language or expression language so that it can be read and processed by a computing device.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## man-made-thing

Athing generated by human activity of some kind. Man-made things include both active things, such as cars or drones, and passive things, such as chairs or trousers.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## mandatory

A requirement that must be implemented in order for an implementer to be in compliance. In ToIP governance frameworks, a mandatory requirement is expressed using a MUST or REQUIRED keyword as defined in IETF RFC 2119.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## message

A discrete unit of communication intended by the source for consumption by some recipient or group of recipients.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## metadata

Information describing the characteristics of data including, for example, structural metadata describing data structures (e.g., data format, syntax, and semantics) and descriptive metadata describing data contents (e.g., information security labels).

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## mobile-deep-link

In the context of mobile apps, deep linking consists of using a uniform resource identifier (URI) that links to a specific location within a mobile app rather than simply launching the app. Deferred deep linking allows users to deep link to content even if the app is not already installed. Depending on the mobile device platform, the URI required to trigger the app may be different.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## mpc

See: multi-party computation.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## multi-party-computation

Secure multi-party computation (also known as secure computation, multi-party computation (MPC) or privacy-preserving computation) is a subfield of cryptography with the goal of creating methods for parties to jointly compute a function over their inputs while keeping those inputs private. Unlike traditional cryptographic tasks, where cryptography assures security and integrity of communication or storage and the adversary is outside the system of participants (an eavesdropper on the sender and receiver), the cryptography in this model protects participants' privacy from each other.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## multi-party-control

A variant of multi-party computation where multiple parties must act in concert to meet a control requirement without revealing each other’s data. All parties are privy to the output of the control, but no party learns anything about the others.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## multi-signature

A cryptographic signature scheme where the process of signing information (e.g., a transaction) is distributed among multiple private keys.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## multicast-address

A multicast address is a logical identifier for a group of hosts in a computer network that are available to process datagrams or frames intended to be multicast for a designated network service.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## multicast

In computer networking, multicast is group communication where data transmission is addressed (using a multicast address) to a group of destination computers simultaneously. Multicast can be one-to-many or many-to-many distribution. Multicast should not be confused with physical layer point-to-multipoint communication.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## natural-person

A person (in legal meaning, one who has its own legal personality) that is an individual human being, as distinguished from the broader category of a legal person, which may refer to either a natural person or an organization of any kind.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## natural-thing

A thing that exists in the natural world independently of humans. Although natural things may form part of a man-made thing, natural things are mutually exclusive with man-made things.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## network-address

A network address is an identifier for a node or host on a telecommunications network. Network addresses are designed to be unique identifiers across the network, although some networks allow for local, private addresses, or locally administered addresses that may not be unique. Special network addresses are allocated as broadcast or multicast addresses. A network address designed to address a single device is called a unicast address.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## nist-csrc

Abbreviation for the NIST Computer Security Resource Center Glossary.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## node

In telecommunications networks, a node (Latin: nodus, ‘knot’) is either a redistribution point or a communication endpoint. The definition of a node depends on the network and protocol layer referred to. A physical network node is an electronic device that is attached to a network, and is capable of creating, receiving, or transmitting information over a communication channel.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## non-custodial-wallet

A digital wallet that is directly in the control of the holder, usually because the holder is the device controller of the device hosting the digital wallet (smartcard, smartphone, tablet, laptop, desktop, car, etc.) A digital wallet that is in the custody of a third party is called a custodial wallet.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## non-repudiable

Non-repudiation refers to a situation where a statement's author **cannot successfully dispute** its authorship or the validity of an associated contract, signature or commitment.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## non-transferable-identifier

Controlling keys over this identifier cannot be rotated and therefore this identifier is non-transferable to other control.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## non-transferable

No transferable (the control over) a certain digital asset in an unobstructed or loss-less manner. As opposed to transferable.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## objective

Something toward which a party (its owner) directs effort (an aim, goal, or end of action).

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## oobi

See: out-of-band introduction.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## openwallet-foundation

A non-profit project of the Linux Foundation chartered to build a world-class open source wallet engine.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## operational-circumstances

In the context of privacy protection, this term denotes the context in which privacy trade-off decisions are made. It includes the regulatory environment and other non-technical factors that bear on what reasonable privacy expectations might be.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## optional

A requirement that is not mandatory or recommended to implement in order for an implementer to be in compliance, but which is left to the implementer’s choice. In ToIP governance frameworks, an optional requirement is expressed using a MAY or OPTIONAL keyword as defined in IETF RFC 2119.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## organization

A party that consists of a group of parties who agree to be organized into a specific form in order to better achieve a common set of objectives. Examples include corporations, partnerships, sole proprietorships, non-profit organizations, associations, and governments.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## organizational-authority

A type of authority where the party asserting its right is an organization.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: True

## out-of-band-introduction

A process by which two or more entities exchange VIDs in order to form a cryptographically verifiable connection (e.g., a ToIP connection), such as by scanning a QR code (in person or remotely) or clicking a deep link.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## owner

The role that a party performs when it is exercising its legal, rightful or natural title to control a specific entity.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## p2p

See: peer-to-peer.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## packet

The logical unit of network communications produced by the transport layer.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## party

An entity that sets its objectives, maintains its knowledge, and uses that knowledge to pursue its objectives in an autonomous (sovereign) manner. Natural persons and organizations are the typical examples.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## password

A string of characters (letters, numbers and other symbols) that are used to authenticate an identity, verify access authorization or derive cryptographic keys.

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: True

## peer-to-peer

Peer-to-peer (P2P) computing or networking is a distributed application architecture that partitions tasks or workloads between peers. Peers are equally privileged, equipotent participants in the network. This forms a peer-to-peer network of nodes.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## peer

In the context of digital networks, an actor on the network that has the same status, privileges, and communications options as the other actors on the network.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: True

## permission

Authorization to perform some action on a system.

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: True

## persistent-connection

A connection that is able to persist across multiple communication sessions. In a ToIP context, a persistent connection is established when two ToIP endpoints exchange verifiable identifiers (VIDs) that they can use to re-establish the connection with each other whenever it is needed.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## persistent-identifier

transferable-identifier

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## person

See natural person.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## personal-data-store

See: personal data vault.

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: False

## personal-data-vault

A digital vault whose controller is a natural person.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## personal-data

Any information relating to an identified or identifiable natural person (called a data subject under GDPR).

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## personal-wallet

A digital wallet whose holder is a natural person.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## personally-identifiable-information

Information (any form of data) that can be used to directly or indirectly identify or re-identify an individual person either singly or in combination within a single record or in correlation with other records. This information can be one or more attributes/fields/properties in a record (e.g., date-of-birth) or one or more records (e.g., medical records).

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## physical-credential

A credential in a physical form such as paper, plastic, or metal.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## pii

See: personally identifiable information.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## pki

See: public key infrastructure.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## plaintext

Unencrypted information that may be input to an encryption operation. Once encrypted, it becomes ciphertext.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## policy

Statements, rules, or assertions that specify required, permitted, prohibited, or expected behavior of an entity within a defined scope. Policies may be human-readable, machine-readable, or both, and may be interpreted, enforced, or audited by people, software, or both.

- Authority scope: policy_definition, assurance_and_audit
- Delegation mode: direct
- Revocation supported: True

## pop

See: proof of personhood.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## presentation-attack

A type of cybersecurity attack in which the attacker attempts to defeat a biometric liveness detection system by providing false inputs.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## presentation-request

A protocol request sent by the verifier to the holder of a digital wallet to request a presentation.

- Authority scope: verification_and_reliance
- Delegation mode: direct
- Revocation supported: False

## presentation

A verifiable message that a holder may send to a verifier containing proofs of one or more claims derived from one or more digital credentials from one or more issuers as a response to a specific presentation request from a  verifier.

- Authority scope: credential_issuance, verification_and_reliance
- Delegation mode: direct
- Revocation supported: True

## primary-document

The governance document at the root of a governance framework. The primary document specifies the other controlled documents in the governance framework.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## principal

The party for whom, or on behalf of whom, an actor is executing an action (this actor is then called an agent of that party).

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: False

## principles-of-ssi

A set of principles for self-sovereign identity systems originally defined by the Sovrin Foundation and republished by the ToIP Foundation.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## privacy-policy

A statement or legal document (in privacy law) that discloses some or all of the ways a party gathers, uses, discloses, and manages a customer or client's data.

- Authority scope: policy_definition
- Delegation mode: direct
- Revocation supported: False

## privacy-washing

De-identification so that it provides a personal data safe harbour and could be legally acceptable forwarded.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## private-key

In public key cryptography, the cryptographic key which must be kept secret by the controller in order to maintain security.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## proof-of-control

See: proof of possession.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## proof-of-personhood

Proof of personhood (PoP) is a means of resisting malicious attacks on peer-to-peer networks, particularly, attacks that utilize multiple fake identities, otherwise known as a Sybil attack. Decentralized online platforms are particularly vulnerable to such attacks by their very nature, as notionally democratic and responsive to large voting blocks. In PoP, each unique human participant obtains one equal unit of voting power, and any associated rewards.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## proof-of-possession

A verification process whereby a level of assurance is obtained that the owner of a key pair actually controls the private key associated with the public key.

- Authority scope: assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## proof-of-presence

See: liveness detection.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## proof

A digital object that enables cryptographic verification of either: a) the claims from one or more digital credentials, or b) facts about claims that do not reveal the data  itself (e.g., proof of the subject being over/under a specific age without revealing a birthdate).

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## property

In the context of digital communication, an attribute of a digital object or data structure, such as a DID document or a schema.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## protected-data

Data that is not publicly available but requires some type of access control to gain access.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## protocol-layer

In modern protocol design, protocols are layered to form a protocol stack. Layering is a design principle that divides the protocol design task into smaller steps, each of which accomplishes a specific part, interacting with the other parts of the protocol only in a small number of well-defined ways. Layering allows the parts of a protocol to be designed and tested without a combinatorial explosion of cases, keeping each design relatively simple.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## protocol-stack

The protocol stack or network stack is an implementation of a computer networking protocol suite or protocol family. Some of these terms are used interchangeably but strictly speaking, the _suite_ is the definition of the communication protocols, and the _stack_ is the software implementation of them.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## pseudonym

A pseudonym is a fictitious name that a person assumes for a particular purpose, which differs from their original or true name (orthonym). This also differs from a new name that entirely or legally replaces an individual's own. Many pseudonym holders use pseudonyms because they wish to remain anonymous, but anonymity is difficult to achieve and often fraught with legal issues.

- Authority scope: verification_and_reliance
- Delegation mode: direct
- Revocation supported: False

## public-key-certificate

A set of data that uniquely identifies a public key (which has a corresponding private key) and an owner that is authorized to use the key pair. The certificate contains the owner’s public key and possibly other information and is digitally signed by a certification authority (i.e., a trusted party), thereby binding the public key to the owner.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: True

## public-key-cryptography

Public key cryptography, or asymmetric cryptography, is the field of cryptographic systems that use pairs of related keys. Each key pair consists of a public key and a corresponding private key. Key pairs are generated with cryptographic algorithms based on mathematical problems termed one-way functions. Security of public key cryptography depends on keeping the private key secret; the public key can be openly distributed without compromising security.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## public-key-infrastructure

A set of policies, processes, server platforms, software and workstations used for the purpose of administering certificates and public-private key pairs, including the ability to issue, maintain, and revoke public key certificates. The PKI includes the hierarchy of certificate authorities that allow for the deployment of digital certificates that support encryption, digital signature and authentication to meet business and security requirements.

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: True

## public-key

In public key cryptography, the cryptographic key that can be freely shared with anyone by the controller without compromising security. A party's public key must be verified as authoritative in order to verify their digital signature.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: False

## qr-code

A QR code (short for "quick-response code") is a type of two-dimensional matrix barcode—a machine-readable optical image that contains information specific to the identified item. In practice, QR codes contain data for a locator, an identifier, and web tracking.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## rbac

See: role-based access control.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## real-world-identity

A term used to describe the opposite of digital identity, i.e., an identity (typically for a person) in the physical instead of the digital world.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## recommended

A requirement that is not mandatory to implement in order for an implementer to be in compliance, but which should be implemented unless the implementer has a good reason. In ToIP governance frameworks, a recommendation is expressed using a SHOULD or RECOMMENDED keyword as defined in IETF RFC 2119.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## record

A uniquely identifiable entry or listing in a database or registry.

- Authority scope: registry_management
- Delegation mode: direct
- Revocation supported: True

## registrant

The party submitting a registration record to a registry.

- Authority scope: registry_management
- Delegation mode: direct
- Revocation supported: True

## registrar

The party who performs registration on behalf of a registrant.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## registration-agent

A party responsible for accepting registration requests and authenticating the registrant. The term may also apply to a party accepting issuance requests for digital credentials.

- Authority scope: credential_issuance, delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: True

## registration

The process by which a registrant submits a record to a registry.

- Authority scope: registry_management
- Delegation mode: direct
- Revocation supported: True

## registry

A specialized database of records that serves as an authoritative source of information about entities.

- Authority scope: registry_management, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## relationship-context

A context established within the boundary of a trust relationship.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## relationship

See ToIP relationship.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## relying-party

A party who accepts claims, credentials, trust graphs, or any other form of verifiable data from other parties (such as issuers, holders, trust registries, or other authoritative sources) in order to make a trust decision.

- Authority scope: credential_issuance, verification_and_reliance, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## reputation-graph

A graph of the reputation relationships between different entities in a trust community. In a digital trust ecosystem, the governing body may be one trust anchor of a reputation graph. In some cases, a reputation graph can be traversed by making queries to one or more trust registries.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## reputation-system

Reputation systems are programs or algorithms that allow users to rate each other in online communities in order to build trust through reputation. Some common uses of these systems can be found on e-commerce websites such as eBay, Amazon.com, and Etsy as well as online advice communities such as Stack Exchange.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## reputation

The beliefs or opinions that are generally held about an entity, typically developed as a result of social evaluation on a set of criteria, such as behavior, performance, or trustworthiness.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## reputational-trust

Established by a trusted party offering identity-assurance.

- Authority scope: assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## requirement

A specified condition or behavior to which a system needs to comply. Technical requirements are defined in technical specifications and implemented in computer systems to be executed by software actors. Governance requirements are defined in governance documents that specify policies and procedures to be executed by human actors. In ToIP specifications, requirements are expressed using the keywords defined in Internet RFC 2119.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: False

## resolver

An entity or component that provides discovery for identifiers. A Resolver is the Controller of its own self-referential identifier which may not be the same as the identifier to which it is a Resolver.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## revocation

In the context of digital credentials, revocation is an event or status change signifying that the issuer no longer attests to the validity of a credential it has issued. In the context of cryptographic keys, revocation is an event or status change signifying that the controller no longer attests to the validity of a public/private key pair for which the controller is authoritative.

- Authority scope: credential_issuance, verification_and_reliance, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## risk-assessment

The process of identifying risks to organizational operations (including mission, functions, image, reputation), organizational assets, individuals, other organizations, and the overall ecosystem, resulting from the operation of an information system. Risk assessment is part of risk management, incorporates threat and vulnerability analyses, and considers risk mitigations provided by security controls planned or in place.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## risk-decision

See: trust decision.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## risk-management

The process of managing risks to organizational operations (including mission, functions, image, or reputation), organizational assets, or individuals resulting from the operation of an information system, and includes: (i) the conduct of a risk assessment; (ii) the implementation of a risk mitigation strategy; and (iii) employment of techniques and procedures for the continuous monitoring of the security state of the information system.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## risk-mitigation

Prioritizing, evaluating, and implementing the appropriate risk-reducing controls/countermeasures recommended from the risk management process.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## risk

The effects that uncertainty (i.e. a lack of information, understanding or knowledge of events, their consequences or likelihoods) can have on the intended realization of an objective of a party.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## role-based-access-control

Access control based on user roles (i.e., a collection of access authorizations a user receives based on an explicit or implicit assumption of a given role). Role permissions may be inherited through a role hierarchy and typically reflect the permissions needed to perform defined functions within an organization. A given role may apply to a single individual or to several individuals.

- Authority scope: access_decisioning
- Delegation mode: direct
- Revocation supported: True

## role-credential

A credential claiming that the subject has a specific role.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## role

A defined set of characteristics that an entity has in some context, such as responsibilities it may have, actions (behaviors) it may execute, or pieces of knowledge that it is expected to have in that context, which are referenced by a specific role name.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## rotation

a change of the key state, including a change to the set of authoritative key pairs for an identifier AID.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: False

## router

A router is a networking device that forwards data packets between computer networks. Routers perform the traffic directing functions between networks and on the global Internet. Data sent through a network, such as a web page or email, is in the form of data packets. A packet is typically forwarded from one router to another router through the networks that constitute an internetwork (e.g. the Internet) until it reaches its destination node. This process is called routing.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## routing

Routing is the process of selecting a path for traffic in a network or between or across multiple networks. Broadly, routing is performed in many types of networks, including circuit-switched networks, such as the public switched telephone network (PSTN), and computer networks, such as the Internet. A router is a computing device that specializes in performing routing.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## rule

A prescribed guide for conduct, process or action to achieve a defined result or objective. Rules may be human-readable or machine-readable or both.

- Authority scope: policy_definition
- Delegation mode: direct
- Revocation supported: False

## rwi

See: real world identity.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## schema

A framework, pattern, or set of rules for enforcing a specific structure on a digital object or a set of digital data. There are many types of schemas, e.g., data schema, credential verification schema, database schema.

- Authority scope: credential_issuance, policy_definition
- Delegation mode: direct
- Revocation supported: True

## scid

See: self-certifying identifier.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## scope

In the context of terminology, scope refers to the set of possible concepts within which: a) a specific term is intended to uniquely identify a concept, or b) a specific glossary is intended to identify a set of concepts. In the context of identification, scope refers to the set of possible entities within which a specific entity must be uniquely identified. In the context of specifications, scope refers to the set of problems (the problem space) within which the specification is intended to specify solutions.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## second-party

The party with whom a first party engages to form a trust relationship, establish a connection, make a delegation, or execute a transaction.

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: True

## secure-attribution

Secure attribution is strongly related to _making and proving statements_. A controller makes statements to the a validator or verifier, who in turn validates the statements issued. A controller "_owns_" the statement: content and attribution via digital signatures. Secure attribution is "whodunit?!" in cyberspace.

- Authority scope: verification_and_reliance
- Delegation mode: direct
- Revocation supported: False

## secure-enclave

A coprocessor on Apple iOS devices that serves as a trusted execution environment.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## secure-multi-party-computation

See: multi-party computation.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## security-domain

An environment or context that includes a set of system resources and a set of system entities that have the right to access the resources as defined by a common security policy, security model, or security architecture.

- Authority scope: policy_definition
- Delegation mode: direct
- Revocation supported: False

## security-policy

A set of policies and rules that governs all aspects of security-relevant system and system element behavior.

- Authority scope: policy_definition
- Delegation mode: direct
- Revocation supported: False

## self-asserted

A term used to describe a claim or a credential whose subject is also the issuer.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## self-certified

When a party provides its own certification that it is compliant with a set of requirements, such as a governance framework. The term is also applied to data structures that are cryptographically verifiable such as self-certifying identifiers.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## self-certifying-identifier

A subclass of verifiable identifier (VID) that is cryptographically verifiable without the need to rely on any third party for verification because the identifier is cryptographically bound to the cryptographic keys from which it was generated.

- Authority scope: verification_and_reliance
- Delegation mode: direct
- Revocation supported: False

## self-sovereign-identity

Self-sovereign identity is a decentralized identity architecture that implements the Principles of SSI — principally that it puts the identity controller (e.g., a natural person or organization) directly in control of the identifiers and credentials they use to assert their digital identity.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## sensitive-data

Personal data that a reasonable person would view from a privacy protection standpoint as requiring special care above and beyond other personal data.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## session

See: communication session.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## single-signature-identifier

or single sig identifier; is an identifier controlled by a one-of-one signing key-pair

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## sociotechnical-system

An approach to complex organizational work design that recognizes the interaction between people and technology in workplaces. The term also refers to coherent systems of human relations, technical objects, and cybernetic processes that inhere to large, complex infrastructures. Social society, and its constituent substructures, qualify as complex sociotechnical systems.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## software-agent

In computer science, a software agent is a computer program that acts for a user or other program in a relationship of agency, which derives from the Latin *agere* (to do): an agreement to act on one's behalf. A user agent is a specific type of software agent that is used directly by an end-user as the principal.

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: False

## sovrin-foundation

A 501 (c)(4) nonprofit organization established to administer the governance framework governing the Sovrin Network, a public service utility enabling self-sovereign identity on the internet. The Sovrin Foundation is an independent organization that is responsible for ensuring the Sovrin identity system is public and globally accessible.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## spanning-layer

A specific layer within a protocol stack that consists of a single protocol explicitly designed to provide interoperability between the protocol layers above it and below it.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## specification

See: technical specification.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## ssi

See: self-sovereign identity.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## stream

In the context of digital communications, and in particular streaming media, a flow of data delivered in a continuous manner from a server to a client rather than in discrete messages.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## streaming-media

Streaming media is multimedia for playback using an offline or online media player. Technically, the stream is delivered and consumed in a continuous manner from a client, with little or no intermediate storage in network elements. Streaming refers to the delivery method of content, rather than the content itself.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## subject

The entity described by one or more claims, particularly in the context of credentials.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## subscription

In the context of decentralized digital trust infrastructure, a subscription is an agreement between a first digital agent—the *publisher*—to automatically send a second digital agent—the *subscriber*—a message when a specific type of event happens in the wallet or vault managed by the first digital agent.

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: False

## supporting-system

A system that operates at ToIP Layer 1, the trust support layer of the ToIP stack. A supporting system is one of three types of systems defined in the ToIP Technology Architecture Specification.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## sybil-attack

A Sybil attack is a type of attack on a computer network service in which an attacker subverts the service's reputation system by creating a large number of pseudonymous identities and uses them to gain a disproportionately large influence. It is named after the subject of the book _Sybil_, a case study of a woman diagnosed with dissociative identity disorder.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## system-of-record

A system of record (SOR) or source system of record (SSoR) is a data management term for an information storage system (commonly implemented on a computer system running a database management system) that is the authoritative source for a given data element or piece of information.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: False

## tamper-evident

A process which makes alterations to the data easily detectable. Form digital data objects, this is typically achieved via cryptographic verification.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## tamper-resistant

A process which makes alterations to data difficult (hard to perform), costly (expensive to perform), or both. For digital data objects, this is typically achieved via cryptographic verification.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## tcp-ip-stack

The protocol stack implementing the TCP/IP suite.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## tcp-ip

See: Internet Protocol Suite.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## technical-requirement

A requirement for a hardware or software component or system. In the context of decentralized digital trust infrastructure, technical requirements are a subset of governance requirements. Technical requirements are often specified in a technical specification.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: False

## technical-specification

A document that specifies, in a complete, precise, verifiable manner, the requirements, design, behavior, or other characteristics of a system or component and often the procedures for determining whether these provisions have been satisfied.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## technical-trust

A level of assurance in a trust relationship that can be achieved only via technical means such as hardware, software, network protocols, and cryptography.Cryptographic trust is a specialized type of technical trust.

- Authority scope: assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## tee

See: trusted execution environment.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## term

A unit of text (i.e., a word or phrase) that is used in a particular context or scope to refer to a concept (or a relation between concepts, or a property of a concept).

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## terminology

Terminology is a group of specialized words and respective meanings in a particular field, and also the study of such terms and their use; the latter meaning is also known as *terminology science*. A term is a word, compound word, or multi-word expressions that in specific contexts is given specific meanings—meaning which may deviate from the meanings the same words have in other contexts and in everyday language. Terminology is a discipline that studies, among other things, the development of such terms and their interrelationships within a specialized domain. Terminology differs from *lexicography*, as the former involves the study of concepts, conceptual systems and their labels (terms), whereas lexicography studies words and their meanings.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## terms-community

A group of parties who share the need for a common terminology.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## terms-wiki

A wiki website used by a terms community to input, maintain, and publish its terminology. The Concepts and Terminology Working Group at the ToIP Foundation has created a simple template for GitHub-based terms wikis.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## thing

An entity that is neither a natural person nor an organization and thus cannot be a party. A thing may be a natural thing or a man-made thing.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## third-party

A party that is not directly involved in the trust relationship between a first party and a second party, but provides supporting services to either or both of them.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## three-party-model

The issuer—holder—verifier model used by all types of physical credentials and digital credentials to enable transitive trust decisions.

- Authority scope: credential_issuance, verification_and_reliance
- Delegation mode: direct
- Revocation supported: True

## timestamp

A token or packet of information that is used to provide assurance of timeliness; the timestamp contains timestamped data, including a time, and a signature generated by a trusted timestamp authority (TTA).

- Authority scope: assurance_and_audit, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## tls

See: Transport Layer Security.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-application

A trust application that runs at ToIP Layer 4, the trust application layer.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-channel

See: ToiP relationship.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-communication

Communication that uses the ToIP stack to deliver ToIP messages between ToIP endpoints, optionally using ToIP intermediaries to provide authenticity, confidentiality, and correlation privacy.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-connection

See: ToIP relationship.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-controller

The controller of a verifiable identifier (VID) used with the ToIP stack.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-endpoint

An endpoint that communicates via the ToIP Trust Spanning Protocol (TSP) as described in the ToIP Technology Architecture Specification.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-foundation

A non-profit project of the Linux Foundation chartered to define an overall architecture for decentralized digital trust infrastructure known as the ToIP stack.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-governance-architecture-specification

The specification defining the requirements for the ToIP Governance Stack published by the ToIP Foundation.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: False

## toip-governance-framework

A governance framework that conforms to the requirements of the ToIP Governance Architecture Specification.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## toip-governance-metamodel

A structural model for governance frameworks that specifies the recommended governance documents that should be included depending on the objectives of the trust community.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## toip-governance-stack

The governance half of the four layer ToIP stack as defined by the ToIP Governance Architecture Specification.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: False

## toip-identifier

A verifiable identifier (VID) for an entity that is addressable using the ToIP stack.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-intermediary

See: intermediary system.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-layer-1

The trust support layer of the ToIP stack, responsible for supporting the trust spanning protocol at ToIP Layer 2.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-layer-2

The trust spanning layer of the ToIP stack, responsible for enabling trust task protocols at ToIP Layer 3.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-layer-3

The trust task layer of the ToIP stack, responsible for enabling trust applications at ToIP Layer 4.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-layer-4

The trust application layer of the ToIP stack, where end-users have the direct human experience of using applications that call trust task protocols to engage in trust relationships and make trust decisions using ToIP decentralized digital trust infrastructure.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-layer

One of four protocol layers in the ToIP stack. The four layers are ToIP Layer 1, ToIP Layer 2, ToIP Layer 3, and ToIP Layer 4.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-message

A message communicated between ToIP endpoints using the ToIP stack. ToIP messages are transmitted over the ToIP Trust Spanning Protocol (TSP) at Layer 2 of the ToIP stack.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-relationship

A VID-to-VID relationship formed between two entities over the ToIP Trust Spanning Protocol.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-specification

A specification published by the ToIP Foundation. ToIP specifications may be in one of three states: *Draft Deliverable*, *Working Group Approved Deliverable*, or *ToIP Approved Deliverable*.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-stack

The layered architecture for decentralized digital trust infrastructure defined by the ToIP Foundation. The ToIP stack is a dual stack consisting of two halves: the ToIP Technology Stack and the ToIP Governance Stack. The four layers in the ToIP stack are ToIP Layer 1, ToIP Layer 2, ToIP Layer 3, and ToIP Layer 4.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: False

## toip-system

A computing system that participates in the ToIP Technology Stack. There are three types of ToIP systems: endpoint systems, intermediary systems, and supporting systems.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-technology-architecture-specification

The technical specification defining the requirements for the ToIP Technology Stack published by the ToIP Foundation.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-technology-stack

The technology half of the four layer ToIP stack as defined by the ToIP Technology Architecture Specification.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-trust-community

A trust community governed by a ToIP governance framework.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## toip-trust-network

A trust network implemented using the ToIP stack.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip-trust-registry-protocol

The open standard trust task protocol defined by the ToIP Foundation to perform the trust task of querying a trust registry. The ToIP Trust Registry Protocol operates at Layer 3 of the ToIP stack.

- Authority scope: registry_management
- Delegation mode: direct
- Revocation supported: True

## toip-trust-spanning-protocol

The ToIP Trust Spanning Protocol (TSP) is the ToIP Layer 2 protocol for verifiable messaging that implements the trust spanning layer of the ToIP stack.  The TSP enables actors in different digital trust domains to interact in a similar way to how the Internet Protocol (IP) enables devices on different local area networks to exchange data.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## toip

See: Trust Over IP

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## transaction

A discrete event between a user and a system that supports a business or programmatic purpose. A digital system may have multiple categories or types of transactions, which may require separate analysis within the overall digital identity risk assessment.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## transferable-identifier

Control over the identifier transferable by [[xref: keri1, rotation]].

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## transferable

Capable of being transferred or conveyed from one place or person to another. Place can be its and bits.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## transitive-trust-decision

A trust decision made by a first party about a second party or another entity based on information about the second party or the other entity that is obtained from one or more third parties.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## transport-layer-security

Transport Layer Security (TLS) is a cryptographic protocol designed to provide communications security over a computer network. The protocol is widely used in applications such as email, instant messaging, and Voice over IP, but its use in securing HTTPS remains the most publicly visible. The TLS protocol aims primarily to provide security, including privacy (confidentiality), integrity, and authenticity through the use of cryptography, such as the use of certificates, between two or more communicating computer applications.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## transport-layer

Layer of the TCP/IP protocol stack that is responsible for reliable connection-oriented or connectionless end-to-end communications.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## tribal-knowledge

Knowledge that is known within an “in-group” of people but unknown outside of it. A tribe, in this sense, is a group of people that share such a common knowledge.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-anchor

The authoritative source that serves as the origin of a trust chain.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: False

## trust-application-layer

In the context of the ToIP stack, the trust application layer is ToIP Layer 4. Applications running at this layer call trust task protocols at ToIP Layer 3.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-application

An application that runs at ToIP Layer 4 in order to perform trust tasks or engage in other verifiable messaging using the ToIP stack.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-assurance

A process that provides a level of assurance sufficient to make a particular trust decision.

- Authority scope: assurance_and_audit
- Delegation mode: direct
- Revocation supported: False

## trust-basis

The properties of a verifiable identifier (VID) or a ToIP system that enable a party to appraise it to determine a trust limit.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-boundary

The border of a trust domain.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-chain

A set of cryptographically verifiable links between digital credentials or other data containers that enable transitive trust decisions.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## trust-community

A set of parties who collaborate to achieve a mutual set of trust objectives.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## trust-context

The context in which a specific party makes a specific trust decision. Many different factors may be involved in establishing a trust context, such as: the relevant interaction or transaction; the presence or absence of existing trust relationships; the applicability of one or more governance frameworks; and the location, time, network, and/or devices involved. A trust context may be implicit or explicit; if explicit, it may be identified using an identifier. A ToIP governance framework is an example of an explicit trust context identified by a verifiable identifier (VID).

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## trust-decision

A decision that a party needs to make about whether to engage in a specific interaction or transaction with another entity that involves real or perceived risks.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-domain

A security domain defined by a computer hardware or software architecture, a security policy, or a trust community, typically via a trust framework or governance framework.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## trust-ecosystem

See digital trust ecosystem.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-establishment

The process two or more parties go through to establish a trust relationship. In the context of decentralized digital trust infrastructure, trust establishment takes place at two levels. At the technical trust level, it includes some form of key establishment. At the human trust level, it may be accomplished via an out-of-band introduction, the exchange of digital credentials, queries to one or more trust registries, or evaluation of some combination of human-readable and machine-readable governance frameworks.

- Authority scope: credential_issuance, policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## trust-factor

A property, relationship, or other signal that can contribute to a party making a trust decision.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-framework

A term (most frequently used in the digital identity industry) to describe a governance framework for a digital identity system, especially a federation.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## trust-graph

A data structure describing the trust relationship between two or more entities. A simple trust graph may be expressed as a trust list. More complex trust graphs can be recorded or registered in and queried from a trust registry. Trust graphs can also be expressed using trust chains and chained credentials. Trust graphs can enable verifiers and relying parties to make transitive trust decisions.

- Authority scope: credential_issuance, verification_and_reliance, registry_management
- Delegation mode: direct
- Revocation supported: True

## trust-limit

A limit to the degree a party is willing to trust an entity in a specific trust relationship within a specific trust context.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-list

A one-dimensional trust graph in which an authoritative source publishes a list of entities that are trusted in a specific trust context. A trust list can be considered a simplified form of a trust registry.

- Authority scope: registry_management, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## trust-network

A network of parties who are connected via trust relationships (such as via a membership agreement) conforming to requirements defined in a legal regulation, trust framework or governance framework. A trust network is more formal than a digital trust ecosystem; the latter may connect parties more loosely via transitive trust relationships and/or across multiple trust networks.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## trust-objective

An objective shared by the parties in a trust community to establish and maintain trust relationships.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-over-ip

A term coined by John Jordan to describe the decentralized digital trust infrastructure made possible by the ToIP stack. A play on the term *Voice over IP* (abbreviated *VoIP*). The term was adopted as the name for the Trust over IP Foundation aka ToIP Foundation.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-registry-protocol

See: ToIP Trust Registry Protocol.

- Authority scope: registry_management
- Delegation mode: direct
- Revocation supported: True

## trust-registry

A registry that serves as an authoritative source for trust graphs or other governed information describing one or more trust communities. A trust registry is typically authorized by a governance framework.

- Authority scope: policy_definition, registry_management, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## trust-relationship

A relationship between a party and an entity in which the party has decided to trust the entity in one or more trust contexts up to a trust limit.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-root

See: trust anchor

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-service-provider

In the context of specific digital trust ecosystems, such as the European Union’s eIDAS regulations, a trust service provider is a legal entity that provides specific trust support services as required by legal regulations, trust frameworks, or governance frameworks. In the larger context of ToIP infrastructure, a trust service provider is a provider of services based on the ToIP stack. Most generally, a trust service provider is to the trust layer for the Internet what an Internet service provider (ISP) is to the Internet layer.

- Authority scope: policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: False

## trust-spanning-layer

A spanning layer designed to span between different digital trust domains. In the ToIP stack, the trust spanning layer is ToIP Layer 2.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-spanning-protocol

See: ToIP Trust Spanning Protocol.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-support-layer

In the context of the ToIP stack, the trust support layer is ToIP Layer 1. It supports the operations of the ToIP Trust Spanning Protocol at ToIP Layer 2.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-support

A system, protocol, or other infrastructure whose function is to facilitate the establishment and maintenance of trust relationships at higher protocol layers. In the ToIP stack, the trust support layer is Layer 1.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-task-layer

In the context of the ToIP stack, the trust task layer is ToIP Layer 3. It supports trust applications operating at ToIP Layer 4.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-task-protocol

A ToIP Layer 3 protocol that implements a specific trust task on behalf of a trust application operating at ToIP Layer 4.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-task

A specific task that involves establishing, verifying, or maintaining trust relationships or exchanging verifiable messages or verifiable data that can be performed on behalf of a trust application by a trust task protocol at Layer 3 of the ToIP stack.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust-triangle

See: three-party model.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trust

A belief that an entity will behave in a predictable manner in specified circumstances. The entity may be a person, process, object or any combination of such components. The entity can be of any size from a single hardware component or software module, to a piece of equipment identified by make and model, to a site or location, to an organization, to a nation-state. Trust, while inherently a subjective determination, can be based on objective evidence and subjective elements. The objective grounds for trust can include for example, the results of information technology product testing and evaluation. Subjective belief, level of comfort, and experience may supplement (or even replace) objective evidence, or substitute for such evidence when it is unavailable. Trust is usually relative to a specific circumstance or situation (e.g., the amount of money involved in a transaction, the sensitivity or criticality of information, or whether safety is an issue with human lives at stake). Trust is generally not transitive (e.g., you trust a friend but not necessarily a friend of a friend). Finally, trust is generally earned, based on experience or measurement.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trusted-execution-environment

A trusted execution environment (TEE) is a secure area of a main processor. It helps code and data loaded inside it to be protected with respect to confidentiality and integrity. Data integrity prevents unauthorized entities from outside the TEE from altering data, while code integrity prevents code in the TEE from being replaced or modified by unauthorized entities, which may also be the computer owner itself as in certain DRM schemes.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trusted-role

A role that performs restricted activities for an organization after meeting competence, security and background verification requirements for that role.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trusted-third-party

In cryptography, a trusted third party (TTP) is an entity which facilitates interactions between two parties who both trust the third party; the third party reviews all critical transaction communications between the parties, based on the ease of creating fraudulent digital content. In TTP models, the relying parties use this trust to secure their own interactions. TTPs are common in any number of commercial transactions and in cryptographic digital transactions as well as cryptographic protocols, for example, a certificate authority (CA) would issue a digital certificate to one of two parties. The CA then becomes the TTP to that certificate's issuance. Likewise transactions that need a third party recordation would also need a third-party repository service of some kind.

- Authority scope: verification_and_reliance, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## trusted-timestamp-authority

An authority that is trusted to provide accurate time information in the form of a timestamp.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: True

## trustworthiness

An attribute of an entity, such as a person or organization, that provides confidence to others of the qualifications, capabilities, and reliability of that entity to perform specific tasks and fulfill assigned responsibilities. Trustworthiness is also a characteristic of information technology products and systems. The attribute of trustworthiness, whether applied to people, processes, or technologies, can be measured, at least in relative terms if not quantitatively. The determination of trustworthiness plays a key role in establishing trust relationships among persons and organizations. The trust relationships are key factors in risk decisions made by senior leaders/executives.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## trustworthy

A property of an entity that has the attribute of trustworthiness.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## tsp

See: ToIP Trust Spanning Protocol.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## tta

See: trusted timestamp authority.

- Authority scope: governance_recognition
- Delegation mode: direct
- Revocation supported: True

## ttp

See: trusted third party.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## udp

See: User Datagram Protocol.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## unicast-address

A network address used for a unicast.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## unicast

In computer networking, unicast is a one-to-one transmission from one point in the network to another point; that is, one sender and one receiver, each identified by a network address (a unicast address). Unicast is in contrast to multicast and broadcast which are one-to-many transmissions. Internet Protocol unicast delivery methods such as Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) are typically used.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## uniform-resource-identifier

A Uniform Resource Identifier (URI) is the generic standard for all types of identifiers used to link resources in the World Wide Web. The most common type of a URI is a URL (Uniform Resource Locator). The URI standard is defined by IETF RFC 3986. URNs (Uniform Resource Names) are another type of URIs intended for persistent identifiers.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## uniform-resource-locator

A Uniform Resource Locator (URL) is the standard form of a Web address used to link resources in browsers and other Internet applications. Technically, it is a specific type of Uniform Resource Identifier (URI).

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## uniform-resource-name

A Uniform Resource Name (URN) is a type of URI (Uniform Resource Identifier) designed for persistent identifiers that are intended to be assigned once to a resource and never changed to identify a different resource. In some cases a URN is also intended to serve as a persistent way to locate the identified resource over time even as it moves locations on the network. The URN standard is defined by IETF RFC 8141.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## uri

See: Uniform Resource Identifier.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## url

See: Uniform Resource Locator.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## urn

See: Uniform Resource Name.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## user-agent

A software agent that is used directly by the end-user as the principal. Browsers, email clients, and digital wallets are all examples of user agents.

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: False

## user-datagram-protocol

In computer networking, the User Datagram Protocol (UDP) is one of the core communication protocols of the Internet protocol suite used to send messages (transported as datagrams in packets) to other hosts on an Internet Protocol (IP) network. Within an IP network, UDP does not require prior communication to set up communication channels or data paths.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## utility-governance-framework

A governance framework for a digital trust utility. A utility governance framework may be a component of or referenced by an ecosystem governance framework or a credential governance framework.

- Authority scope: credential_issuance, policy_definition, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## validation

An action an agent (of a principal) performs to determine whether a digital object or set of data meets the requirements of a specific party.

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: False

## vault

See: digital vault.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## vc

See: verifiable credential.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## verifiable-credential

A standard data model and representation format for cryptographically-verifiable digital credentials as defined by the W3C Verifiable Credentials Data Model Specification.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## verifiable-data-registry

A registry that facilitates the creation, verification, updating, and/or deactivation of decentralized identifiers and DID documents. A verifiable data registry may also be used for other cryptographically-verifiable data structures such as verifiable credentials.

- Authority scope: credential_issuance, registry_management
- Delegation mode: direct
- Revocation supported: True

## verifiable-data

Any digital data or object that is digitally signed in such a manner that it can be cryptographically verified.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## verifiable-identifier

An identifier over which the controller can provide cryptographic proof of control. Each type of VID defines a specific means for discovering the public key, network endpoints, or other metadata necessary to prove control. Decentralized identifiers (DIDs) are a W3C standard for VIDs. VIDs are the cryptographically verifiable identifiers used in the ToIP stack.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## verifiable-message

A message communicated as verifiable data by virtue of being digitally signed.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## verifiable

In the context of digital communications infrastructure, the ability to determine the authenticity of a communication (e.g., sender, contents, claims, metadata, provenance), or the underlying sociotechnical infrastructure (e.g., governance, roles, policies, authorizations, certifications).

- Authority scope: credential_issuance, access_decisioning, governance_recognition
- Delegation mode: direct
- Revocation supported: True

## verification

An action an agent (of a principal) performs to determine the authenticity of a claim or other data object. Cryptographic verification uses cryptographic keys.

- Authority scope: credential_issuance, delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: False

## verifier

A role an agent performs to verify one or more proofs of the claims in a digital credential or other verifiable data, and to evaluate whether the presented material satisfies applicable verification and policy criteria.

- Authority scope: credential_issuance, verification_and_reliance, policy_definition, delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: True

## vid-relationship

The communications relationship formed between two VIDs using the ToIP Trust Spanning Protocol. A particular feature of this protocol is its ability to establish as many VID relationships as needed to establish different relationship contexts between the communicating entities.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## vid-to-vid

The specialized type of peer-to-peer communications enabled by the ToIP Trust Spanning Protocol. Each pair of VIDs creates a unique VID relationship.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## vid

See ​​verifiable identifier.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## virtual-credential

Digital representations of claims or identity attributes, often used in online environments.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## virtual-vault

A digital vault enclosed inside another digital vault by virtue of having its own verifiable identifier (VID) and its own set of encryption keys that are separate from those used to unlock the enclosing vault.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## voice-over-ip

Voice over Internet Protocol (VoIP), also called IP telephony, is a method and group of technologies for voice calls for the delivery of voice communication sessions over Internet Protocol (IP) networks, such as the Internet.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## voip

See: Voice over IP.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## w3c-verifiable-credentials-data-model-specification

A W3C Recommendation defining a standard data model and representation format for cryptographically-verifiable digital credentials. Version 1.1 was published on 03 March 2022.

- Authority scope: credential_issuance
- Delegation mode: direct
- Revocation supported: True

## wallet-engine

The set of software components that form the core of a digital wallet, but which by themselves are not sufficient to deliver a fully functional wallet for use by a digital agent (of a principal). A wallet engine is to a digital wallet what a browser engine is to a web browser.

- Authority scope: delegation_and_scope
- Delegation mode: direct_or_constrained
- Revocation supported: False

## wallet

See: digital wallet.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## witness

A computer system that receives, verifies, and stores proofs of key events for a verifiable identifier (especially an autonomic identifier). Each witness controls its own verifiable identifier used to sign key event messages stored by the witness. A witness may use any suitable computer system or database architecture, including a file, centralized database, distributed database, distributed ledger, or blockchain.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## zero-knowledge-proof

A specific kind of cryptographic proof that proves facts about data to a verifier without revealing the underlying data itself. A common example is proving that a person is over or under a specific age without revealing the person’s exact birthdate.

- Authority scope: verification_and_reliance
- Delegation mode: direct
- Revocation supported: False

## zero-knowledge-service-provider

The provider of a zero-knowledge service that hosts encrypted data on behalf of the principal but does not have access to the private keys in order to be able to decrypt it.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## zero-knowledge-service

In cloud computing, the term “zero-knowledge” refers to an online service that stores, transfers or manipulates data in a way that maintains a high level of confidentiality, where the data is only accessible to the data's owner (the client), and not to the service provider. This is achieved by encrypting the raw data at the client's side or end-to-end (in case there is more than one client), without disclosing the password to the service provider. This means that neither the service provider, nor any third party that might intercept the data, can decrypt and access the data without prior permission, allowing the client a higher degree of privacy than would otherwise be possible. In addition, zero-knowledge services often strive to hold as little metadata as possible, holding only that data that is functionally needed by the service.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## zero-trust-architecture

A network security architecture based on the core design principle “never trust, always verify”, so that all actors are denied access to resources pending verification.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False

## zkp

See: zero-knowledge proof.

- Authority scope: terminology_definition
- Delegation mode: direct
- Revocation supported: False
