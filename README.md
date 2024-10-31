# spec-u-llm

Using LLMs to update the [Filecoin specification](https://spec.filecoin.io/). A
Fast Phil experiment from the [2024 Chiang Mai Filecoin Hacker
House](https://filecoin.notion.site/Filecoin-Hacker-House-Runbook-10a7631f282580dcb872d18bac5959ee).

## The Problem

The [Filecoin specification](https://spec.filecoin.io/) is a complex document
that was originally crafted to aid the development of Lotus (and other Filecoin
implementations) before Filecoin mainnet launch.   

As the network has evolved, the effective consensus system has been modified,
primarily through [Filecoin Improvement Proposals
(FIPs)](https://github.com/filecoin-project/FIPs). The written spec has not
kept up with these developments (though most of the changes are minor).

## AI FIXES THIS!

Well, not quite: but the challenge is that the individuals knowledgeable enough
to edit the spec are also in demand for many other purposes. The aim here is to
make the job of managing updates as easy as possible, and preferably to
generalise the burden away from these domain experts.

## What specullm does

Specullm takes a FIP as an argument, and runs the text of the FIP through an
llm, optionally prefixed with the text of the specification (or selected parts
of the specification), and a prompt. 

## Sample workflow

[SPECIFICATION] + [FIP]  +
"Enumerate the changes to the specification implied by this FIP, and give the
filenames that of the parts of the spec affected by that change."

                |
                |
                v

(for each change)
[FILES AFFECTED BY CHANGE] + [ENUMERATED CHANGE] + [FIP] +
"Suggest text that would make the above specification extracts be consistent
with this new FIP"
                
                |
                |
                v

(for each text)
[FILES AFFECTED BY CHANGE] + [SUGGESTED TEXT] + "Produce this in the form of a diff"





















