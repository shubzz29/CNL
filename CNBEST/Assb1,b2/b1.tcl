#Create a simulator object
set ns [new Simulator]

#Define different colors for data flows (for NAM)
$ns color 1 Blue

#Open the NAM trace file
set nf [open out.nam w]
$ns namtrace-all $nf

#Define a 'finish' procedure
proc finish {} {
        global ns nf
        $ns flush-trace
        #Close the NAM trace file
        close $nf
        #Execute NAM on the trace file
        exec nam out.nam &
        exit 0
}

#Create three nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]

#Create links between the nodes
$ns duplex-link $n0 $n1 1.7Mb 10ms DropTail
$ns duplex-link $n1 $n2 2Mb 10ms DropTail
#$ns duplex-link $n2 $n3 1.7Mb 20ms DropTail

#Set Queue Size of link (n1-n0) to 5
$ns queue-limit $n1 $n0 5

#Give node position (for NAM)
$ns duplex-link-op $n2 $n1 orient right-down
#$ns duplex-link-op $n1 $n2 orient right-up
$ns duplex-link-op $n1 $n0 orient right

#Monitor the queue for link (n1-n0). (for NAM)
$ns duplex-link-op $n1 $n0 queuePos 0.5


#Setup a TCP connection
set tcp [new Agent/TCP]
$tcp set class_ 2
$ns attach-agent $n2 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n0 $sink
$ns connect $tcp $sink
$tcp set fid_ 1

#Setup a FTP over TCP connection
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP



#Schedule events for the CBR and FTP agents
#$ns at 0.1 "$cbr start"
$ns at 0.5 "$ftp start"
$ns at 2.0 "$ftp stop"
#$ns at 4.5 "$cbr stop"

#Detach tcp and sink agents (not really necessary)
#$ns at 4.5 "$ns detach-agent $n2 $tcp ; $ns detach-agent $n0 $sink"

#Call the finish procedure after 5 seconds of simulation time
$ns at 2.3 "finish"



#Run the simulation
$ns run

