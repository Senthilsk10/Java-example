const imageUpload = document.getElementById('imageUpload')
const message = document.getElementById('message');
Promise.all([
  faceapi.nets.faceRecognitionNet.loadFromUri('https://raw.githubusercontent.com/Senthilsk10/face-api-web/main/models/'),
  faceapi.nets.faceLandmark68Net.loadFromUri('https://raw.githubusercontent.com/Senthilsk10/face-api-web/main/models/'),
  faceapi.nets.ssdMobilenetv1.loadFromUri('https://raw.githubusercontent.com/Senthilsk10/face-api-web/main/models/')
]).then(start)

async function start() {
  const container = document.createElement('div')
  container.style.position = 'relative'
  document.body.append(container)
  const labeledFaceDescriptors = await loadLabeledImages()
  const faceMatcher = new faceapi.FaceMatcher(labeledFaceDescriptors, 0.6)
  let image
  let canvas
  console.log('loaded');
  message.innerText = "Model loaded now you can start upload photos";
  //document.body.append('Loaded')
  imageUpload.addEventListener('change', async () => {
    if (image) image.remove()
    if (canvas) canvas.remove()
    //image = await faceapi.bufferToImage(imageUpload.files[0])
    //container.append(image)
    //canvas = faceapi.createCanvasFromMedia(image)
    //container.append(canvas)
    const displaySize = { width: image.width, height: image.height }
    //faceapi.matchDimensions(canvas, displaySize)
    const detections = await faceapi.detectAllFaces(image).withFaceLandmarks().withFaceDescriptors()
    const resizedDetections = faceapi.resizeResults(detections, displaySize)
    const results = resizedDetections.map(d => faceMatcher.findBestMatch(d.descriptor))
    const queryParams = getQueryParams(queryString);
    const key = queryParams['key'];
    postData(results,key)
    const dl = document.createElement('dl');

    results.forEach((result, i) => {
        dl.innerHTML += `<dt>Serial Number ${i + 1}</dt><dd>${result.toString()}</dd>`;
    });

    document.body.appendChild(dl); 

  })
}

function loadLabeledImages() {

  const labels = ['2238010017','2238010042','2238010058','2238010080']
  return Promise.all(
    labels.map(async label => {
      const descriptions = []
      for (let i = 1; i <= 2; i++) {
        
        const img = await faceapi.fetchImage(`https://raw.githubusercontent.com/Senthilsk10/face-api-web/main/labeled_images/${label}/${i}.jpeg`)
        const detections = await faceapi.detectSingleFace(img).withFaceLandmarks().withFaceDescriptor()
        descriptions.push(detections.descriptor)
      }

      return new faceapi.LabeledFaceDescriptors(label, descriptions)
    })
  )
}

// Get the full query string from the URL
const queryString = window.location.search;

// Use a function to parse the query string into an object
const getQueryParams = (queryString) => {
  const params = {};
  const searchParams = new URLSearchParams(queryString);

  for (const [key, value] of searchParams.entries()) {
    params[key] = value;
  }

  return params;
};


function postData(results, key) {
  const url = '{% url "get_result" %}';
  const labels = results.map(result => result.label); 
  console.log(labels);
  $.ajax({
    url: url,
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify({ "key": key, "labels": labels }), 
    success: function(response) {
      console.log('Success:', response);
    },
    error: function(error) {
      console.error('Error:', error);
    }
  });
}



