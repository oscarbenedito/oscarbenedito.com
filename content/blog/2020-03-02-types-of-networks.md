---
title: "Centralized, decentralized and distributed networks"
categories: knowledge base
tags: ["Networks", "Communications", "Decentralization", "Centralization", "Distributed networks"]
---
When we are trying to understand a communications network, having an approximate image of how the network operates can be very valuable. Do all communications go through the same node? Is there a central authority? Can nodes communicate directly with each other? Depending on how the network operates, we can classify it as centralized, decentralized or distributed.

### Centralized networks

When all the nodes on a network are connected to one unique node, we call it a centralized network. All communications happen through that one "master" node. An example of a centralized network is the one created by most instant messengers, for example [Signal](https://signal.org/). Every time we send a message, it goes to Signal's servers and it is then sent to its destination. This creates a network similar to the following, where everyone is connected to one server (or cluster of servers).

<p style="text-align: center"><svg class="basic-svg" viewBox="0 0 633.9 523.77"><use xlink:href="/img/blog/2020/03/types-of-networks/centralized-network.svg#l"></use></svg></p>

Having everything go through the same computer has its pros and cons. On the one hand, it makes deployment easier and faster, data consistency is easy to maintain and it is an efficient network (if, for instance, you need to gather data, it is all in one server). On the other hand, it creates a single point of failure for the whole network (which also facilitates censorship) and it makes it easier to abuse users (as the central server has a monopoly over the network)[^common]. This type of network also makes escalation much harder, as the resources are provided by one sole party.

[^common]: This is pretty usual. Whether it is services selling user's data, censoring content, a sudden rise of prices, etc., when dealing with centralized services, users don't have much choice but to leave the network completely (which might not be affordable).

### Decentralized networks

Decentralized networks don't have one central node, but multiple of them, which are connected between themselves. When clients connect to the network, their communications go through their "master" node, to the destination's "master" node, and finally to the destination. An example of a decentralized network is [e-mail](https://en.wikipedia.org/wiki/Email). When Alice (`alice@example.com`) wants to send an e-mail to Bob (`bob@example.org`), Alice's computer sends the message to `example.com`'s server. From there, it is sent to `example.org`, and finally `example.org` sends it to Bob's computer. A decentralized network looks similar to the following network.

<p style="text-align: center"><svg class="basic-svg" viewBox="0 0 633.9 523.77"><use xlink:href="/img/blog/2020/03/types-of-networks/decentralized-network.svg#l"></use></svg></p>

Decentralized networks solve some of the centralization problems: no entity has control over the whole network anymore, allowing users to choose between different providers and switch servers (or self-host) if one starts abusing its power. If a server is down, others can still communicate ordinarily, which also makes censorship more difficult. Decentralized networks are also easier to escalate. Nonetheless, this type of network requires more infrastructure and can become less efficient for certain operations (like global tasks). It is also harder to deploy updates, as servers might update at different times, when each administrator decides to do so.

### Distributed networks

Distributed networks only have one type of node, and they are connected with each other (although not necessarily all with all). This creates a very robust network where all nodes are client and server at the same time. The [BitTorrent protocol](https://en.wikipedia.org/wiki/BitTorrent) is an example of a protocol that works with a distributed network. The following image shows what a distributed network looks like.

<p style="text-align: center"><svg class="basic-svg" viewBox="0 0 633.9 523.77"><use xlink:href="/img/blog/2020/03/types-of-networks/distributed-network.svg#l"></use></svg></p>

Because there are no central servers, distributed networks easily circumvent censorship and are practically immune to denial-of-service attacks. Since every user is client and server at the same time, these networks are highly scalable without the need for additional central resources. However, distributed networks make deployment a lot harder.

## Final comments

I hope this post has clarified the main differences between centralized, decentralized and distributed networks as well as showed some applications for each of them. In the future, I might refer to this post when talking about services and the type of network they rely on.
