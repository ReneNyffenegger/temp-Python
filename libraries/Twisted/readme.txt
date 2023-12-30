Twisted is a platform for developing internet applications.

Twisted is a good (if somewhat idiosyncratic) pure-python framework or library, depending on how you treat it, and it continues to improve.

twisted.internet.protocol.Protocol
  Your protocol handling class will usually subclass twisted.internet.protocol.Protocol
  Most protocol handlers inherit either from this class or from one of its convenience children.
  An instance of the protocol class is instantiated per-connection, on demand, and will go away when the connection is finished.
  This means that persistent configuration is not saved in the Protocol.

twisted.internet.protocol.Factory
  The persistent configuration is kept in a Factory class, which usually inherits from
  twisted.internet.protocol.Factory
  The buildProtocol() method of the Factory is used to create a Protocol for each new connection.

