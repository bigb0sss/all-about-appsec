public class InternalHealthCheckController : Controller
{
    public IActionResult Index(String url)
    {
        String[] allowList = { "10.120.1.2", "10.120.1.3" };

        IPHostEntry ip = Dns.GetHostEntry(new Uri(url).Host);

        if (ip.AddressList.Length != 1 || !allowList.Contains(ip.AddressList.GetValue(0).ToString()))
        {
            return BadRequest("Forbidden destination!");
        }
        Thread.Sleep(1000); // Some CPU intensive task...
        var response = WebRequest.Create(url).GetResponse();
        var dataStream = response.GetResponseStream();
        var reader = new StreamReader(dataStream);
        string responseFromServer = reader.ReadToEnd();
        return Content(responseFromServer);
    }
}

/*

# Link
https://twitter.com/SonarSource/status/1468248939379847168

# Issues
1) DNS Rebinding - An attacker can bypass the allowlist by DNS rebining to perform an SSRF attack. You all found it! This risk of DNS rebinding is always easy to overlook: Dns.GetHostEntry() does a first DNS query, validates the result against the allowlist, and then WebRequest does a second DNS query.


# Mitigations
1) Update the DNS validation process.

*/