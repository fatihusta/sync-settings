import sync.registrar

sync.registrar.register_operation("update-hostname",    None, ["hostname -F /etc/hostname"],          1, "restart-networking")
sync.registrar.register_operation("restart-networking", ["ifdown -a -v --exclude=lo"], ["ifup -a -v --exclude=lo", "/usr/bin/systemctl-wait"], 10, None)
sync.registrar.register_operation("restart-dnsmasq",    None, ["/etc/untangle/post-network-hook.d/990-restart-dnsmasq", "/usr/bin/systemctl-wait"],   20, "restart-networking")
sync.registrar.register_operation("restart-miniupnpd",  None, ["/etc/untangle/post-network-hook.d/990-restart-upnp", "/usr/bin/systemctl-wait"],      21, "restart-networking")
sync.registrar.register_operation("restart-radvd",      None, ["/etc/untangle/post-network-hook.d/990-restart-radvd", "/usr/bin/systemctl-wait"],     22, "restart-networking")
sync.registrar.register_operation("restart-ddclient",   None, ["/etc/untangle/post-network-hook.d/990-restart-ddclient", "/usr/bin/systemctl-wait"],  23, "restart-networking")
sync.registrar.register_operation("restart-softflowd",  None, ["/etc/untangle/post-network-hook.d/990-restart-softflowd", "/usr/bin/systemctl-wait"], 25, "restart-networking")
sync.registrar.register_operation("restart-quagga",     None, ["/etc/untangle/post-network-hook.d/990-restart-quagga", "/usr/bin/systemctl-wait"],    26, None)
sync.registrar.register_operation("restart-suricata",   None, ["/etc/untangle/iptables-rules.d/740-suricata", "/usr/bin/systemctl-wait"],             27, None)
sync.registrar.register_operation("restart-keepalived", None, ["/etc/untangle/post-network-hook.d/200-vrrp", "/usr/bin/systemctl-wait"],              30, "restart-networking")
sync.registrar.register_operation("restart-iptables",   None, ["/etc/untangle/post-network-hook.d/960-iptables", "/usr/bin/systemctl-wait"],          50, "restart-networking")
sync.registrar.register_operation("restart-bdamserver", None, ["ps awwwux | grep -q [b]damserver && systemctl restart untangle-bdamserver", "/usr/bin/systemctl-wait"],                  51, None)
sync.registrar.register_operation("apt-update",         None, ["apt-get update", "/usr/bin/systemctl-wait"],                                              52, None)
sync.registrar.register_operation("restart-pyconnector",None, ["ps awwwux | grep -q [p]yconnector && systemctl restart untangle-pyconnector", "/usr/bin/systemctl-wait"],                                              53, None)
sync.registrar.register_operation("geoip-update",       None, ["/usr/bin/systemctl-wait"],                                              54, None)
sync.registrar.register_operation("restart-wireguard",  None, ["/usr/bin/systemctl-wait"],                                              55, None)
sync.registrar.register_operation("logrotate-test",     None, ["/usr/bin/systemctl-wait"],                                              56, None)
