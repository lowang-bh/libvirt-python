#!/usr/bin/python -u
#
# Those are the autogenerated Python bindings for libvirt.
# Check python/generator.py in the source distribution of libvir
# to find out more about the generation process
#
import libvirtmod
import types

# The root of all libvirt errors.
class libvirtError(Exception):
    def __init__(self, msg, conn=None, dom=None, net=None):
        Exception.__init__(self, msg)

        if dom is not None:
            conn = dom._conn
        elif net is not None:
            conn = net._conn

        if conn is None:
            self.err = virGetLastError()
        else:
            self.err = conn.virConnGetLastError()

    def get_error_code(self):
        if self.err is None:
            return None
        return self.err[0]

    def get_error_domain(self):
        if self.err is None:
            return None
        return self.err[1]

    def get_error_message(self):
        if self.err is None:
            return None
        return self.err[2]

    def get_error_level(self):
        if self.err is None:
            return None
        return self.err[3]

    def get_str1(self):
        if self.err is None:
            return None
        return self.err[4]

    def get_str2(self):
        if self.err is None:
            return None
        return self.err[5]

    def get_str3(self):
        if self.err is None:
            return None
        return self.err[6]

    def get_int1(self):
        if self.err is None:
            return None
        return self.err[7]

    def get_int2(self):
        if self.err is None:
            return None
        return self.err[8]

    def __str__(self):
        if self.get_error_message() is None:
            return Exception.__str__(self)
        else:
            return Exception.__str__(self) + " " + self.get_error_message()

#
# register the libvirt global error handler
#
def registerErrorHandler(f, ctx):
    """Register a Python written function to for error reporting.
       The function is called back as f(ctx, error), with error
       being a list of informations about the error being raised.
       Returns 1 in case of success."""
    return libvirtmod.virRegisterErrorHandler(f,ctx)

#
# Return library version.
#
def getVersion (name = None):
    """If no name parameter is passed (or name is None) then the
    version of the libvirt library is returned as an integer.

    If a name is passed and it refers to a driver linked to the
    libvirt library, then this returns a tuple of (library version,
    driver version).

    If the name passed refers to a non-existent driver, then you
    will get the exception 'no support for hypervisor'.

    Versions numbers are integers: 1000000*major + 1000*minor + release."""
    if name is None:
        ret = libvirtmod.virGetVersion ();
    else:
        ret = libvirtmod.virGetVersion (name);
    if ret is None: raise libvirtError ("virGetVersion() failed")
    return ret


# WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING
#
# Everything before this line comes from libvir.py
# Everything after this line is automatically generated
#
# WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING
#
# Functions from module libvirt
#

def open(name):
    """This function should be called first to get a connection to
       the Hypervisor and xen store """
    ret = libvirtmod.virConnectOpen(name)
    if ret is None:raise libvirtError('virConnectOpen() failed')
    return virConnect(_obj=ret)

def openReadOnly(name):
    """This function should be called first to get a restricted
       connection to the libbrary functionalities. The set of
       APIs usable are then restricted on the available methods
       to control the domains. """
    ret = libvirtmod.virConnectOpenReadOnly(name)
    if ret is None:raise libvirtError('virConnectOpenReadOnly() failed')
    return virConnect(_obj=ret)

def virInitialize():
    """Initialize the library. It's better to call this routine at
       startup in multithreaded applications to avoid potential
       race when initializing the library. """
    ret = libvirtmod.virInitialize()
    if ret == -1: raise libvirtError ('virInitialize() failed')
    return ret

#
# Functions from module virterror
#

def virGetLastError():
    """Provide a pointer to the last error caught at the library
       level Simpler but may not be suitable for multithreaded
       accesses, in which case use virCopyLastError() """
    ret = libvirtmod.virGetLastError()
    return ret

def virResetLastError():
    """Reset the last error caught at the library level. """
    libvirtmod.virResetLastError()

class virDomain:
    def __init__(self, conn, _obj=None):
        self._conn = conn
        if _obj != None:self._o = _obj;return
        self._o = None

    def __del__(self):
        if self._o != None:
            libvirtmod.virDomainFree(self._o)
        self._o = None

    #
    # virDomain functions from module libvirt
    #

    def ID(self):
        """Get the hypervisor ID number for the domain """
        ret = libvirtmod.virDomainGetID(self._o)
        return ret

    def OSType(self):
        """Get the type of domain operation system. """
        ret = libvirtmod.virDomainGetOSType(self._o)
        if ret is None: raise libvirtError ('virDomainGetOSType() failed', dom=self)
        return ret

    def UUIDString(self, buf):
        """Get the UUID for a domain as string. For more information
           about UUID see RFC4122. """
        ret = libvirtmod.virDomainGetUUIDString(self._o, buf)
        if ret == -1: raise libvirtError ('virDomainGetUUIDString() failed', dom=self)
        return ret

    def XMLDesc(self, flags):
        """Provide an XML description of the domain. The description
           may be reused later to relaunch the domain with
           virDomainCreateLinux(). """
        ret = libvirtmod.virDomainGetXMLDesc(self._o, flags)
        if ret is None: raise libvirtError ('virDomainGetXMLDesc() failed', dom=self)
        return ret

    def attachDevice(self, xml):
        """Create a virtual device attachment to backend. """
        ret = libvirtmod.virDomainAttachDevice(self._o, xml)
        if ret == -1: raise libvirtError ('virDomainAttachDevice() failed', dom=self)
        return ret

    def coreDump(self, to, flags):
        """This method will dump the core of a domain on a given file
           for analysis. Note that for remote Xen Daemon the file
           path will be interpreted in the remote host. """
        ret = libvirtmod.virDomainCoreDump(self._o, to, flags)
        if ret == -1: raise libvirtError ('virDomainCoreDump() failed', dom=self)
        return ret

    def create(self):
        """launch a defined domain. If the call succeed the domain
           moves from the defined to the running domains pools. """
        ret = libvirtmod.virDomainCreate(self._o)
        if ret == -1: raise libvirtError ('virDomainCreate() failed', dom=self)
        return ret

    def destroy(self):
        """Destroy the domain object. The running instance is shutdown
           if not down already and all resources used by it are given
           back to the hypervisor. The data structure is freed and
           should not be used thereafter if the call does not return
           an error. This function may requires priviledged access """
        ret = libvirtmod.virDomainDestroy(self._o)
        if ret == -1: raise libvirtError ('virDomainDestroy() failed', dom=self)
        self._o = None
        return ret

    def detachDevice(self, xml):
        """Destroy a virtual device attachment to backend. """
        ret = libvirtmod.virDomainDetachDevice(self._o, xml)
        if ret == -1: raise libvirtError ('virDomainDetachDevice() failed', dom=self)
        return ret

    def maxMemory(self):
        """Retrieve the maximum amount of physical memory allocated to
           a domain. If domain is None, then this get the amount of
           memory reserved to Domain0 i.e. the domain where the
           application runs. """
        ret = libvirtmod.virDomainGetMaxMemory(self._o)
        if ret == 0: raise libvirtError ('virDomainGetMaxMemory() failed', dom=self)
        return ret

    def maxVcpus(self):
        """Provides the maximum number of virtual CPUs supported for
           the guest VM. If the guest is inactive, this is basically
           the same as virConnectGetMaxVcpus. If the guest is running
           this will reflect the maximum number of virtual CPUs the
           guest was booted with. """
        ret = libvirtmod.virDomainGetMaxVcpus(self._o)
        if ret == -1: raise libvirtError ('virDomainGetMaxVcpus() failed', dom=self)
        return ret

    def name(self):
        """Get the public name for that domain """
        ret = libvirtmod.virDomainGetName(self._o)
        return ret

    def pinVcpu(self, vcpu, cpumap, maplen):
        """Dynamically change the real CPUs which can be allocated to
           a virtual CPU. This function requires priviledged access
           to the hypervisor. """
        ret = libvirtmod.virDomainPinVcpu(self._o, vcpu, cpumap, maplen)
        if ret == -1: raise libvirtError ('virDomainPinVcpu() failed', dom=self)
        return ret

    def reboot(self, flags):
        """Reboot a domain, the domain object is still usable there
           after but the domain OS is being stopped for a restart.
           Note that the guest OS may ignore the request. """
        ret = libvirtmod.virDomainReboot(self._o, flags)
        if ret == -1: raise libvirtError ('virDomainReboot() failed', dom=self)
        return ret

    def resume(self):
        """Resume an suspended domain, the process is restarted from
           the state where it was frozen by calling
           virSuspendDomain(). This function may requires priviledged
           access """
        ret = libvirtmod.virDomainResume(self._o)
        if ret == -1: raise libvirtError ('virDomainResume() failed', dom=self)
        return ret

    def save(self, to):
        """This method will suspend a domain and save its memory
           contents to a file on disk. After the call, if successful,
           the domain is not listed as running anymore (this may be a
           problem). Use virDomainRestore() to restore a domain after
           saving. """
        ret = libvirtmod.virDomainSave(self._o, to)
        if ret == -1: raise libvirtError ('virDomainSave() failed', dom=self)
        return ret

    def setAutostart(self, autostart):
        """Configure the domain to be automatically started when the
           host machine boots. """
        ret = libvirtmod.virDomainSetAutostart(self._o, autostart)
        if ret == -1: raise libvirtError ('virDomainSetAutostart() failed', dom=self)
        return ret

    def setMaxMemory(self, memory):
        """Dynamically change the maximum amount of physical memory
           allocated to a domain. If domain is None, then this change
           the amount of memory reserved to Domain0 i.e. the domain
           where the application runs. This function requires
           priviledged access to the hypervisor. """
        ret = libvirtmod.virDomainSetMaxMemory(self._o, memory)
        if ret == -1: raise libvirtError ('virDomainSetMaxMemory() failed', dom=self)
        return ret

    def setMemory(self, memory):
        """Dynamically change the target amount of physical memory
           allocated to a domain. If domain is None, then this change
           the amount of memory reserved to Domain0 i.e. the domain
           where the application runs. This function may requires
           priviledged access to the hypervisor. """
        ret = libvirtmod.virDomainSetMemory(self._o, memory)
        if ret == -1: raise libvirtError ('virDomainSetMemory() failed', dom=self)
        return ret

    def setVcpus(self, nvcpus):
        """Dynamically change the number of virtual CPUs used by the
           domain. Note that this call may fail if the underlying
           virtualization hypervisor does not support it or if
           growing the number is arbitrary limited. This function
           requires priviledged access to the hypervisor. """
        ret = libvirtmod.virDomainSetVcpus(self._o, nvcpus)
        if ret == -1: raise libvirtError ('virDomainSetVcpus() failed', dom=self)
        return ret

    def shutdown(self):
        """Shutdown a domain, the domain object is still usable there
           after but the domain OS is being stopped. Note that the
           guest OS may ignore the request.  TODO: should we add an
           option for reboot, knowing it may not be doable in the
           general case ? """
        ret = libvirtmod.virDomainShutdown(self._o)
        if ret == -1: raise libvirtError ('virDomainShutdown() failed', dom=self)
        return ret

    def suspend(self):
        """Suspends an active domain, the process is frozen without
           further access to CPU resources and I/O but the memory
           used by the domain at the hypervisor level will stay
           allocated. Use virDomainResume() to reactivate the domain.
           This function may requires priviledged access. """
        ret = libvirtmod.virDomainSuspend(self._o)
        if ret == -1: raise libvirtError ('virDomainSuspend() failed', dom=self)
        return ret

    def undefine(self):
        """undefine a domain but does not stop it if it is running """
        ret = libvirtmod.virDomainUndefine(self._o)
        if ret == -1: raise libvirtError ('virDomainUndefine() failed', dom=self)
        return ret

    #
    # virDomain functions from module python
    #

    def UUID(self):
        """Extract the UUID unique Identifier of a domain. """
        ret = libvirtmod.virDomainGetUUID(self._o)
        if ret is None: raise libvirtError ('virDomainGetUUID() failed', dom=self)
        return ret

    def autostart(self):
        """Extract the autostart flag for a domain """
        ret = libvirtmod.virDomainGetAutostart(self._o)
        if ret == -1: raise libvirtError ('virDomainGetAutostart() failed', dom=self)
        return ret

    def info(self):
        """Extract informations about a domain. Note that if the
           connection used to get the domain is limited only a
           partial set of the informations can be extracted. """
        ret = libvirtmod.virDomainGetInfo(self._o)
        if ret is None: raise libvirtError ('virDomainGetInfo() failed', dom=self)
        return ret

class virNetwork:
    def __init__(self, conn, _obj=None):
        self._conn = conn
        if _obj != None:self._o = _obj;return
        self._o = None

    def __del__(self):
        if self._o != None:
            libvirtmod.virNetworkFree(self._o)
        self._o = None

    #
    # virNetwork functions from module libvirt
    #

    def UUIDString(self, buf):
        """Get the UUID for a network as string. For more information
           about UUID see RFC4122. """
        ret = libvirtmod.virNetworkGetUUIDString(self._o, buf)
        if ret == -1: raise libvirtError ('virNetworkGetUUIDString() failed', net=self)
        return ret

    def XMLDesc(self, flags):
        """Provide an XML description of the network. The description
           may be reused later to relaunch the network with
           virNetworkCreateXML(). """
        ret = libvirtmod.virNetworkGetXMLDesc(self._o, flags)
        if ret is None: raise libvirtError ('virNetworkGetXMLDesc() failed', net=self)
        return ret

    def bridgeName(self):
        """Provides a bridge interface name to which a domain may
           connect a network interface in order to join the network. """
        ret = libvirtmod.virNetworkGetBridgeName(self._o)
        if ret is None: raise libvirtError ('virNetworkGetBridgeName() failed', net=self)
        return ret

    def create(self):
        """Create and start a defined network. If the call succeed the
           network moves from the defined to the running networks
           pools. """
        ret = libvirtmod.virNetworkCreate(self._o)
        if ret == -1: raise libvirtError ('virNetworkCreate() failed', net=self)
        return ret

    def destroy(self):
        """Destroy the network object. The running instance is
           shutdown if not down already and all resources used by it
           are given back to the hypervisor. The data structure is
           freed and should not be used thereafter if the call does
           not return an error. This function may requires
           priviledged access """
        ret = libvirtmod.virNetworkDestroy(self._o)
        if ret == -1: raise libvirtError ('virNetworkDestroy() failed', net=self)
        self._o = None
        return ret

    def name(self):
        """Get the public name for that network """
        ret = libvirtmod.virNetworkGetName(self._o)
        if ret is None: raise libvirtError ('virNetworkGetName() failed', net=self)
        return ret

    def setAutostart(self, autostart):
        """Configure the network to be automatically started when the
           host machine boots. """
        ret = libvirtmod.virNetworkSetAutostart(self._o, autostart)
        if ret == -1: raise libvirtError ('virNetworkSetAutostart() failed', net=self)
        return ret

    def undefine(self):
        """Undefine a network but does not stop it if it is running """
        ret = libvirtmod.virNetworkUndefine(self._o)
        if ret == -1: raise libvirtError ('virNetworkUndefine() failed', net=self)
        return ret

    #
    # virNetwork functions from module python
    #

    def UUID(self):
        """Extract the UUID unique Identifier of a network. """
        ret = libvirtmod.virNetworkGetUUID(self._o)
        if ret is None: raise libvirtError ('virNetworkGetUUID() failed', net=self)
        return ret

    def autostart(self):
        """Extract the autostart flag for a network. """
        ret = libvirtmod.virNetworkGetAutostart(self._o)
        if ret == -1: raise libvirtError ('virNetworkGetAutostart() failed', net=self)
        return ret

    def networkLookupByUUID(self, uuid):
        """Try to lookup a network on the given hypervisor based on
           its UUID. """
        ret = libvirtmod.virNetworkLookupByUUID(self._o, uuid)
        if ret is None:raise libvirtError('virNetworkLookupByUUID() failed', net=self)
        __tmp = virNetwork(self, _obj=ret)
        return __tmp

class virConnect:
    def __init__(self, _obj=None):
        if _obj != None:self._o = _obj;return
        self._o = None

    def __del__(self):
        if self._o != None:
            libvirtmod.virConnectClose(self._o)
        self._o = None

    #
    # virConnect functions from module libvirt
    #

    def createLinux(self, xmlDesc, flags):
        """Launch a new Linux guest domain, based on an XML
           description similar to the one returned by
           virDomainGetXMLDesc() This function may requires
           priviledged access to the hypervisor. """
        ret = libvirtmod.virDomainCreateLinux(self._o, xmlDesc, flags)
        if ret is None:raise libvirtError('virDomainCreateLinux() failed', conn=self)
        __tmp = virDomain(self,_obj=ret)
        return __tmp

    def createXML(self, xmlDesc):
        """Create and start a new virtual network, based on an XML
           description similar to the one returned by
           virNetworkGetXMLDesc() """
        ret = libvirtmod.virNetworkCreateXML(self._o, xmlDesc)
        if ret is None:raise libvirtError('virNetworkCreateXML() failed', conn=self)
        __tmp = virNetwork(self, _obj=ret)
        return __tmp

    def defineXML(self, xml):
        """define a domain, but does not start it """
        ret = libvirtmod.virDomainDefineXML(self._o, xml)
        if ret is None:raise libvirtError('virDomainDefineXML() failed', conn=self)
        __tmp = virDomain(self,_obj=ret)
        return __tmp

    def getCapabilities(self):
        """Provides capabilities of the hypervisor / driver. """
        ret = libvirtmod.virConnectGetCapabilities(self._o)
        if ret is None: raise libvirtError ('virConnectGetCapabilities() failed', conn=self)
        return ret

    def getMaxVcpus(self, type):
        """Provides the maximum number of virtual CPUs supported for a
           guest VM of a specific type. The 'type' parameter here
           corresponds to the 'type' attribute in the <domain>
           element of the XML. """
        ret = libvirtmod.virConnectGetMaxVcpus(self._o, type)
        if ret == -1: raise libvirtError ('virConnectGetMaxVcpus() failed', conn=self)
        return ret

    def getType(self):
        """Get the name of the Hypervisor software used. """
        ret = libvirtmod.virConnectGetType(self._o)
        if ret is None: raise libvirtError ('virConnectGetType() failed', conn=self)
        return ret

    def lookupByID(self, id):
        """Try to find a domain based on the hypervisor ID number """
        ret = libvirtmod.virDomainLookupByID(self._o, id)
        if ret is None:raise libvirtError('virDomainLookupByID() failed', conn=self)
        __tmp = virDomain(self,_obj=ret)
        return __tmp

    def lookupByName(self, name):
        """Try to lookup a domain on the given hypervisor based on its
           name. """
        ret = libvirtmod.virDomainLookupByName(self._o, name)
        if ret is None:raise libvirtError('virDomainLookupByName() failed', conn=self)
        __tmp = virDomain(self,_obj=ret)
        return __tmp

    def lookupByUUIDString(self, uuidstr):
        """Try to lookup a domain on the given hypervisor based on its
           UUID. """
        ret = libvirtmod.virDomainLookupByUUIDString(self._o, uuidstr)
        if ret is None:raise libvirtError('virDomainLookupByUUIDString() failed', conn=self)
        __tmp = virDomain(self,_obj=ret)
        return __tmp

    def networkDefineXML(self, xml):
        """Define a network, but does not create it """
        ret = libvirtmod.virNetworkDefineXML(self._o, xml)
        if ret is None:raise libvirtError('virNetworkDefineXML() failed', conn=self)
        __tmp = virNetwork(self, _obj=ret)
        return __tmp

    def networkLookupByName(self, name):
        """Try to lookup a network on the given hypervisor based on
           its name. """
        ret = libvirtmod.virNetworkLookupByName(self._o, name)
        if ret is None:raise libvirtError('virNetworkLookupByName() failed', conn=self)
        __tmp = virNetwork(self, _obj=ret)
        return __tmp

    def networkLookupByUUIDString(self, uuidstr):
        """Try to lookup a network on the given hypervisor based on
           its UUID. """
        ret = libvirtmod.virNetworkLookupByUUIDString(self._o, uuidstr)
        if ret is None:raise libvirtError('virNetworkLookupByUUIDString() failed', conn=self)
        __tmp = virNetwork(self, _obj=ret)
        return __tmp

    def numOfDefinedDomains(self):
        """Provides the number of inactive domains. """
        ret = libvirtmod.virConnectNumOfDefinedDomains(self._o)
        if ret == -1: raise libvirtError ('virConnectNumOfDefinedDomains() failed', conn=self)
        return ret

    def numOfDefinedNetworks(self):
        """Provides the number of inactive networks. """
        ret = libvirtmod.virConnectNumOfDefinedNetworks(self._o)
        if ret == -1: raise libvirtError ('virConnectNumOfDefinedNetworks() failed', conn=self)
        return ret

    def numOfDomains(self):
        """Provides the number of active domains. """
        ret = libvirtmod.virConnectNumOfDomains(self._o)
        if ret == -1: raise libvirtError ('virConnectNumOfDomains() failed', conn=self)
        return ret

    def numOfNetworks(self):
        """Provides the number of active networks. """
        ret = libvirtmod.virConnectNumOfNetworks(self._o)
        if ret == -1: raise libvirtError ('virConnectNumOfNetworks() failed', conn=self)
        return ret

    def restore(self, frm):
        """This method will restore a domain saved to disk by
           virDomainSave(). """
        ret = libvirtmod.virDomainRestore(self._o, frm)
        if ret == -1: raise libvirtError ('virDomainRestore() failed', conn=self)
        return ret

    #
    # virConnect functions from module python
    #

    def getInfo(self):
        """Extract hardware informations about the Node. """
        ret = libvirtmod.virNodeGetInfo(self._o)
        if ret is None: raise libvirtError ('virNodeGetInfo() failed', conn=self)
        return ret

    def listDefinedDomains(self):
        """list the defined domains, stores the pointers to the names
           in @names """
        ret = libvirtmod.virConnectListDefinedDomains(self._o)
        if ret is None: raise libvirtError ('virConnectListDefinedDomains() failed', conn=self)
        return ret

    def listDefinedNetworks(self):
        """list the defined networks, stores the pointers to the names
           in @names """
        ret = libvirtmod.virConnectListDefinedNetworks(self._o)
        if ret is None: raise libvirtError ('virConnectListDefinedNetworks() failed', conn=self)
        return ret

    def listDomainsID(self):
        """Returns the list of the ID of the domains on the hypervisor """
        ret = libvirtmod.virConnectListDomainsID(self._o)
        if ret is None: raise libvirtError ('virConnectListDomainsID() failed', conn=self)
        return ret

    def listNetworks(self):
        """list the networks, stores the pointers to the names in
           @names """
        ret = libvirtmod.virConnectListNetworks(self._o)
        if ret is None: raise libvirtError ('virConnectListNetworks() failed', conn=self)
        return ret

    def lookupByUUID(self, uuid):
        """Try to lookup a domain on the given hypervisor based on its
           UUID. """
        ret = libvirtmod.virDomainLookupByUUID(self._o, uuid)
        if ret is None:raise libvirtError('virDomainLookupByUUID() failed', conn=self)
        __tmp = virDomain(self,_obj=ret)
        return __tmp

    #
    # virConnect functions from module virterror
    #

    def virConnGetLastError(self):
        """Provide a pointer to the last error caught on that
           connection Simpler but may not be suitable for
           multithreaded accesses, in which case use
           virConnCopyLastError() """
        ret = libvirtmod.virConnGetLastError(self._o)
        return ret

    def virConnResetLastError(self):
        """Reset the last error caught on that connection """
        libvirtmod.virConnResetLastError(self._o)

# virErrorLevel
VIR_ERR_NONE = 0
VIR_ERR_WARNING = 1
VIR_ERR_ERROR = 2

# virDomainState
VIR_DOMAIN_NOSTATE = 0
VIR_DOMAIN_RUNNING = 1
VIR_DOMAIN_BLOCKED = 2
VIR_DOMAIN_PAUSED = 3
VIR_DOMAIN_SHUTDOWN = 4
VIR_DOMAIN_SHUTOFF = 5
VIR_DOMAIN_CRASHED = 6

# virDeviceMode
VIR_DEVICE_DEFAULT = 0
VIR_DEVICE_RO = 1
VIR_DEVICE_RW = 2
VIR_DEVICE_RW_FORCE = 3

# virErrorDomain
VIR_FROM_NONE = 0
VIR_FROM_XEN = 1
VIR_FROM_XEND = 2
VIR_FROM_XENSTORE = 3
VIR_FROM_SEXPR = 4
VIR_FROM_XML = 5
VIR_FROM_DOM = 6
VIR_FROM_RPC = 7
VIR_FROM_PROXY = 8
VIR_FROM_CONF = 9
VIR_FROM_QEMU = 10
VIR_FROM_NET = 11
VIR_FROM_TEST = 12
VIR_FROM_REMOTE = 13

# virDomainRestart
VIR_DOMAIN_DESTROY = 1
VIR_DOMAIN_RESTART = 2
VIR_DOMAIN_PRESERVE = 3
VIR_DOMAIN_RENAME_RESTART = 4

# virErrorNumber
VIR_ERR_OK = 0
VIR_ERR_INTERNAL_ERROR = 1
VIR_ERR_NO_MEMORY = 2
VIR_ERR_NO_SUPPORT = 3
VIR_ERR_UNKNOWN_HOST = 4
VIR_ERR_NO_CONNECT = 5
VIR_ERR_INVALID_CONN = 6
VIR_ERR_INVALID_DOMAIN = 7
VIR_ERR_INVALID_ARG = 8
VIR_ERR_OPERATION_FAILED = 9
VIR_ERR_GET_FAILED = 10
VIR_ERR_POST_FAILED = 11
VIR_ERR_HTTP_ERROR = 12
VIR_ERR_SEXPR_SERIAL = 13
VIR_ERR_NO_XEN = 14
VIR_ERR_XEN_CALL = 15
VIR_ERR_OS_TYPE = 16
VIR_ERR_NO_KERNEL = 17
VIR_ERR_NO_ROOT = 18
VIR_ERR_NO_SOURCE = 19
VIR_ERR_NO_TARGET = 20
VIR_ERR_NO_NAME = 21
VIR_ERR_NO_OS = 22
VIR_ERR_NO_DEVICE = 23
VIR_ERR_NO_XENSTORE = 24
VIR_ERR_DRIVER_FULL = 25
VIR_ERR_CALL_FAILED = 26
VIR_ERR_XML_ERROR = 27
VIR_ERR_DOM_EXIST = 28
VIR_ERR_OPERATION_DENIED = 29
VIR_ERR_OPEN_FAILED = 30
VIR_ERR_READ_FAILED = 31
VIR_ERR_PARSE_FAILED = 32
VIR_ERR_CONF_SYNTAX = 33
VIR_ERR_WRITE_FAILED = 34
VIR_ERR_XML_DETAIL = 35
VIR_ERR_INVALID_NETWORK = 36
VIR_ERR_NETWORK_EXIST = 37
VIR_ERR_SYSTEM_ERROR = 38
VIR_ERR_RPC = 39
VIR_ERR_GNUTLS_ERROR = 40
VIR_WAR_NO_NETWORK = 41

# virDomainCreateFlags
VIR_DOMAIN_NONE = 0

# virSchedParameterType
VIR_DOMAIN_SCHED_FIELD_INT = 1
VIR_DOMAIN_SCHED_FIELD_UINT = 2
VIR_DOMAIN_SCHED_FIELD_LLONG = 3
VIR_DOMAIN_SCHED_FIELD_ULLONG = 4
VIR_DOMAIN_SCHED_FIELD_DOUBLE = 5
VIR_DOMAIN_SCHED_FIELD_BOOLEAN = 6

# virVcpuState
VIR_VCPU_OFFLINE = 0
VIR_VCPU_RUNNING = 1
VIR_VCPU_BLOCKED = 2

