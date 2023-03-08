<h1>Cloud Resume Challenge</h1>

<h2><a href="https://www.jakeespinosa.com/">Check Out The Live Project!</a></h2>

<h2>Description</h2>
<p>
<a href="https://cloudresumechallenge.dev/docs/the-challenge/aws/">The Cloud Resume Challenge</a> is a serverless full-stack resume website hosted in AWS. I implemented a front-end, REST API, <a href="https://github.com/jakeEspinosa/visitorCountAPI">back-end</a>, and CI/CD pipeline as part of the challenge.
</p>

<p>
The website displays my resume and keeps track of how many hits it gets, as detailed by the Visitor Counter.
</p>

<p>
The website is fully serverless, using S3 and CloudFront to serve static content, an API Gateway to facilitate RESTful communication with the Lambda back-end, and a DynamoDB database to store the visitor count. GitHub Actions is configured to automatically push my code to S3 and invalidate the CloudFront cache when I push to the main branch of this repository.
</p>

<h2>Languages Used:</h2>

- Python
- JavaScript
- HTML
- CSS

<h2>Platforms Used:</h2>

- AWS Lambda
- AWS DynamoDB
- AWS API Gateway
- AWS S3
- AWS CloudFront
- GitHub Actions
