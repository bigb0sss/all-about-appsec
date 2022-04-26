import { Request, Response, Application } from 'express';
import  express from 'express';
import db from './postgres';

const FORBIDDEN_CHARS = /['\\]/g;
const isForbidden = (str: string) => FORBIDDEN_CHARS.test(str);

const app: Application = express();

app.get('/api/users/:name', async (req: Request, res: Response) => {
    const { name } = req.params;
    if (isForbidden(name)) {
        return res.sendStatus(400);
    }
    const user = await db.query(`SELECT * FROM users WHERE name='${name}'`);
    res.join(user);
});

app.listen(1337);


/*

# Link
https://twitter.com/SonarSource/status/1468973725072564225

# Issues
1) SQL Injection - The escape characters were set right; however, there was a bug with `g` that it makes the regex object retain the last match index and will continue after that index when .test() is called again. We can still send quotes 2 times to abuse this bug to cause the SQLi.

# Mitigations
1) Use alternative way to sanitize the user inputs.

*/