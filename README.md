# PyHaier - AC Remote

## Beware: WIP

## Intro
Local Haier AC remote, based **heavily** on [@bstuff job with TypeScript](https://github.com/bstuff/haier-ac-remote).

Current version is being able to parse "State" packets from the AC, allowing us to get info as power state, temps and more.

The AC itself is TCP listening on 56800, sending data when a connection is established and every few seconds when the AC is powered on.

## How to run?
Install python *construct* library using `pip install construct`.
Change the AC's IP address in the `test.py` file (MAC is not required right now) and run it.

## What about Haier's cloud service?
Data is being sent by default to *gw.haieriot.com*, their cloud service, along with local TCP connections.
There is no issue to continue use their service, but as many people are concerned about privacy and external services, blocking the cloud service is a possibility.
I recommend *PiHole* or any custom inhouse DNS service will allow you to alter it and block their default cloud service inhouse).
Of course you can also block the IP addresses too within your router's firewall.

## Home Assistant Integration?
I'd really like that, and that's the main reason for the Python port. There's a HomeBridge solution to that using the original repo but I wanted a cleaner solution.

## What next?
Next steps include implementing sending commands feature to the AC (porting the TypeScript code too from @bstuff repo), and HomeAssistant integrations.

## Contribution?
I'd love that. Any help would be great.