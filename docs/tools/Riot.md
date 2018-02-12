Riot
===

The chat client that comes by default with this repository provides various
powerful features like federation, communication in big groups, and end2end
encryption.

End2End encryption
---

The end2end encryption ins Riot is still in a beta state. This makes it
difficult to already using it in production.

If you want to try it, should know it's based on the same concept as
[Signal] uses. Right now, it's quite difficult to chat with this feature
enabled because everyone in a conversation has to verify every device of
every conversation partner.

This leads to a exploding number of validations which is simply not possible
to handle. This again leads to very weak validations which again make it
easy for an attacker to compromise to conversation.

When a device is not verified, it won't get any of the sent messages.

As already pointed out, the feature is still in beta state and the problems
are well known. They should be fixed in future and this way provide secure
communication for large scale communities over multiple servers and empower
secure collaboration.

Federation
---

Matrix currently most powerful feature is the ability to work federated. It
allows to communicate with all kinds of communities without registering
every time. Which lowers the barrier to participate and improves collaboration.

It also allows file sharing and video conferencing with all people in a
channel.

To use the feature you can simply use the Matrix addresses of rooms or people:

```
Room:
#matrix@matrix.org

User:
@someone@matrix.org
```

---

Additional information:

- https://opensource.com/article/17/5/introducing-riot-IRC
- https://matrix.org/blog/posts/


[Signal]: https://signal.org
