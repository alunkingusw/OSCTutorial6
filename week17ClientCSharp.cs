using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        // IP address of the remote computer
        string remoteIP = "localhost";
        // Port number of the remote computer
        int remotePort = 2000;
        // Message to send
        string message = "Hello from C#";

        // Create a new socket
        Socket sender = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

        try
        {
            // Connect to the remote computer
            sender.Connect(remoteIP, remotePort);
            // Encode the message as a byte array
            byte[] msg = Encoding.UTF8.GetBytes(message);
            // Send the message
            int bytesSent = sender.Send(msg);

            Console.WriteLine("Message sent successfully");
            byte[] replyBytes = new byte[1024];

            int bytesReceived = sender.Receive(replyBytes);
            // Decode the reply
            string reply = Encoding.UTF8.GetString(replyBytes, 0, bytesReceived);

            Console.WriteLine("Reply from remote: " + reply);
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error: " + ex.Message);
        }
        finally
        {
            // Close the socket
            sender.Shutdown(SocketShutdown.Both);
            sender.Close();
        }
    }
}
