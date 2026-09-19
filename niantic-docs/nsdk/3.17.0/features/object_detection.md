---
source: https://www.nianticspatial.com/docs/nsdk/3.17.0/features/object_detection/
title: Object Detection
---

<div class="docContentTransition">

<div class="theme-doc-markdown markdown">

<div>

# Object Detection

</div>

With over 200 new classes of objects, the Object Detection subsystem enhances Lightship's contextual awareness capabilities by creating semantically labeled 2D bounding boxes that dynamically update as real-world objects appear on-screen. For each bounding box, the subsystem processes the central square crop of the image, then makes an independent prediction for every subclass and returns the probability that the detected object belongs to each of them. Lightship Object Detection also provides the following model card which explains how detections were trained for person, a human hand, or a human face.

<div style="text-align:center">

<img src="https://www.nianticspatial.com/docs/assets/images/object_detection_feature-2d867484e4e170b7f02f175e60ee946e.gif" width="600" alt="Image with Bounding Boxes around Detected Objects" />

</div>

## Basic Usage<a href="#basic-usage" class="hash-link" aria-label="Direct link to Basic Usage" title="Direct link to Basic Usage">​</a>

By placing Lightship's `ARObjectDetectionManager` in a scene and subscribing to the `ObjectDetectionsUpdated` event, developers can receive realtime detection information in the form of [XRDetectedObjects](https://www.nianticspatial.com/docs/nsdk/3.17.0/apiref/Niantic/Lightship/AR/XRSubsystems/XRDetectedObject/). You can also listen for the `MetadataInitialized` event to receive the list of object classes when the model becomes available to use.

The frame rate of the `ARObjectDetectionManager` can also be adjusted to save performance or detect objects at a faster rate.

## Object Detection Categories<a href="#object-detection-categories" class="hash-link" aria-label="Direct link to Object Detection Categories" title="Direct link to Object Detection Categories">​</a>

There are 206 different categories that the neural network looks for inside a bounding box.

Category List

<div>

<div class="collapsibleContent_i85q">

| Category | Description |
|----|----|
| human_face | human face |
| human_hand | human hand |
| person | person, man, woman, boy, girl, human body |
| skull | skull |
| aircraft | aircraft, airplane, helicopter, rocket, parachute |
| bicycle | bicycle, stationary bicycle, unicycle |
| boat | boat, watercraft, barge, gondola, canoe, jet ski, submarine, personal flotation device |
| bus | bus |
| car | car, snowmobile, golf cart, tank, snowplow, ambulance, van, limousine, taxi, bus, truck |
| cart | cart |
| motorcycle | motorcycle |
| taxi | taxi |
| train | train |
| truck | truck |
| vehicle | vehicle, car, land vehicle, snowmobile, golf cart, tank, train, snowplow, ambulance, bicycle, unicycle |
| wheel | wheel, tire, bicycle wheel |
| wheelchair | wheelchair |
| bench | bench |
| billboard | billboard, scoreboard |
| christmas_tree | christmas_tree |
| door | door |
| door_handle | door_handle |
| fire_hydrant | fire_hydrant |
| flag | flag |
| parking_meter | parking_meter |
| poster | poster, picture frame |
| sculpture | sculpture, bust, bronze sculpture |
| street_light | street_light |
| traffic_light | traffic_light |
| traffic_sign | traffic_sign, stop sign |
| waste_container | waste_container, garbage bin, trash can |
| water_feature | water_feature, swimming_pool, jacuzzi, fountain |
| window | window (both indoor and outdoor) |
| backpack | backpack |
| clothing | clothing, sports uniform |
| coat | coat, jacket |
| dress | dress |
| fedora | fedora, sun hat, cowboy hat |
| footwear | footwear, roller skates, boot, high heels, sandal |
| glasses | glasses, sunglasses, goggles |
| handbag | handbag, briefcase, picnic basket, luggage and bags |
| headwear | headwear, hat, cowboy hat, fedora, sombrero, sun hat, swim cap, helmet, bicycle helmet, football helmet |
| roller_skates | roller_skates |
| shirt | shirt |
| shorts | shorts |
| skirt | skirt, miniskirt |
| sock | sock |
| suit | suit |
| suitcase | suitcase, briefcase |
| tie | tie |
| trousers | trousers, jeans |
| umbrella | umbrella |
| baseball_bat | baseball_bat |
| baseball_glove | baseball_glove |
| football | football (soccer) |
| frisbee | frisbee, flying disc |
| kite | kite |
| paddle | paddle |
| rugby_ball | rugby_ball |
| skateboard | skateboard |
| skis | skis, ski |
| snowboard | snowboard |
| sports_ball | sports_ball, ball, football, cricket ball, volleyball, tennis ball, rugby ball |
| surfboard | surfboard |
| tennis_ball | tennis_ball |
| tennis_racket | tennis_racket, table tennis racket, racket |
| accordion | accordion |
| brass_instrument | brass_instrument, french horn, saxophone, trombone, trumpet |
| drum | drum |
| flute | flute, harmonica, oboe |
| guitar | guitar |
| musical_instrument | musical_instrument, organ, banjo, cello, drum, french horn, guitar, harp, harpsichord, harmonica, oboe, |
| piano | piano, organ, harpsichord, musical keyboard |
| string_instrument | string_instrument, guitar, banjo, cello, harp, violin |
| violin | violin |
| apple | apple |
| banana | banana |
| berry | berry, strawberry, raspberry |
| broccoli | broccoli |
| carrot | carrot |
| citrus | citrus, orange, lemon, grapefruit |
| coconut | coconut |
| egg | egg |
| food | food, fast food, hot dog, french fries, waffle, pancake, burrito, snack, pretzel, popcorn, cookie, |
| grape | grape |
| mushroom | mushroom |
| pear | pear |
| pumpkin | pumpkin, squash |
| tomato | tomato |
| drink | drink, beer, cocktail, coffee, juice, tea, wine, bottle |
| hot_drink | hot_drink, tea, coffee |
| juice | juice |
| bread | bread |
| cake | cake, tart, muffin |
| cheese | cheese |
| dessert | dessert, ice cream, cake, dessert, muffin, doughnut, donut, bagel, cookie, biscuit, waffle, pancake, |
| donut | donut, doughnut, bagel, pretzel |
| fast_food | fast_food, hot_dog, french_fries, pizza, burrito, hamburger, sandwich |
| french_fries | french_fries |
| hamburger | hamburger |
| hot_dog | hot_dog |
| ice_cream | ice_cream |
| pizza | pizza |
| sandwich | sandwich, submarine sandwich, burrito |
| sushi | sushi |
| bed | bed, infant bed, dog bed |
| chair | chair, stool |
| couch | couch, sofa, studio couch, loveseat, sofa bed |
| furniture | furniture, chair, cabinetry, desk, wine rack, couch, sofa bed, loveseat, wardrobe, nightstand, |
| shelves | shelves, wine rack, bookcase, spice rack |
| storage_cabinet | storage_cabinet, wardrobe, cupboard, closet, cabinetry, filing cabinet, chest of drawers, bathroom cabinet |
| table | table, dining table, desk, table, coffee table, kitchen table, billiard table, countertop, nightstand, |
| bathtub | bathtub |
| fireplace | fireplace, wood-burning stove |
| microwave | microwave, microwave oven |
| oven | oven |
| refrigerator | refrigerator |
| screen | screen, tv, television, computer monitor, tablet computer |
| sink | sink |
| tap | tap, shower |
| toaster | toaster |
| toilet | toilet, bidet |
| balloon | balloon |
| barrel | barrel |
| book | book |
| bottle | bottle |
| bowl | bowl, mixing bowl |
| box | box |
| camera | camera, binoculars |
| candle | candle |
| cannon | cannon |
| chopsticks | chopsticks |
| clock | clock, wall clock, alarm clock |
| coin | coin |
| computer_keyboard | computer_keyboard, keyboard |
| computer_mouse | computer_mouse |
| cooking_pan | cooking_pan, frying pan, wok, waffle iron, slow cooker, pressure cooker |
| cup | cup, mug, coffee cup |
| curtain | curtain, window blind |
| doll | doll |
| flowerpot | flowerpot, vase |
| fork | fork |
| hair_dryer | hair_dryer |
| headphones | headphones |
| jug | jug, measuring cup, teapot, cocktail shaker, pitcher, beaker, kettle |
| knife | knife, kitchen knife, pizza cutter, chisel, dagger, sword |
| lamp | lamp, lantern, candle, light bulb, flashlight, torch, ceiling fan |
| laptop | laptop |
| microphone | microphone |
| pen | pen, pencil |
| phone | phone, telephone, cell phone, mobile phone, smartphone, corded phone, ipod |
| pillow | pillow |
| plate | plate, saucer, platter, cake stand |
| potted_plant | potted_plant, houseplant |
| remote | remote, remote control |
| scissors | scissors |
| snowman | snowman |
| spoon | spoon, ladle, spatula |
| teapot | teapot, kettle |
| teddy_bear | teddy_bear |
| tin_can | tin_can, cooking spray |
| toothbrush | toothbrush |
| toy | toy, doll, dice, flying disc, teddy bear |
| watch | watch |
| wine_glass | wine_glass |
| flower | flower |
| rose | rose |
| sunflower | sunflower |
| animal | animal, squid, shellfish, oyster, lobster, shrimp, crab, bird, magpie, woodpecker, blue jay, ostrich, |
| bird | bird, magpie, woodpecker, blue jay, ostrich, penguin, raven, chicken, eagle, owl, duck, canary, goose, |
| parrot | parrot |
| water_bird | water_bird, duck, goose, swan |
| butterfly | butterfly, moths and butterflies |
| insect | insect, tick, centipede, isopod, bee, beetle, ladybug, ant, moths and butterflies, caterpillar, butterfly |
| dolphin | dolphin |
| fish | fish, goldfish, shark, "Rays and Skates", seahorse, squid |
| goldfish | goldfish |
| jellyfish | jellyfish |
| seal | seal, sea lion, harbor seal, walrus |
| shellfish | shellfish, lobster, oyster, shrimp, crab, starfish, snail |
| whale | whale |
| alpaca | alpaca |
| bear | bear, brown bear |
| big_cat | big_cat, lynx, jaguar, tiger, lion, leopard, cheetah |
| camel | camel |
| cat | cat |
| cow | cow, bull, cattle |
| crocodile | crocodile, alligator |
| deer | deer, antelope |
| dog | dog |
| elephant | elephant |
| frog | frog |
| giraffe | giraffe |
| hippopotamus | hippopotamus |
| horse | horse, donkey, mule |
| kangaroo | kangaroo |
| panda | panda |
| pig | pig |
| polar_bear | polar_bear |
| rabbit | rabbit |
| reptile | reptile, lizard, snake, turtle, tortoise, sea turtle, crocodile, frog |
| rhinoceros | rhinoceros |
| sheep | sheep, goat |
| squirrel | squirrel |
| turtle | turtle, tortoise, sea turtle |
| zebra | zebra |

</div>

</div>

<div class="theme-admonition theme-admonition-note admonition_xJq3 alert alert--secondary">

<div class="admonitionHeading_Gvgb">

<span class="admonitionIcon_Rf37">![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)</span>note

</div>

<div class="admonitionContent_BuS1">

Some of these categories are also covered under one of the other 206 categories; for example, "cat," "dog," and a few others fall under the "animal" category. The neural network makes an independent prediction for each of the 206 categories. For example, the neural network will predict that the bounding box of a cat is both a "cat" and "animal" with relatively high, but likely different, confidences, and it's not guaranteed that one will always be predicted with higher confidence than the other. So if your application is looking for a specifc type of object (in this case, either "cat" or "animal"), make sure to check the first several most confidence categorizations for each bounding box instead of only the most confidence categorization.

</div>

</div>

Super-categories List

<div>

<div class="collapsibleContent_i85q">

| Categories | Covers |
|----|----|
| car | car, taxi |
| vehicle | vehicle, car, train, bicycle, taxi, motorcycle, bus, truck |
| footwear | footwear, roller skates |
| headwear | headwear, fedora |
| sports ball | sports ball, football, rugby ball, tennis ball |
| musical instrument | brass instrument, string instrument, piano, accordion, drum, flute |
| string instrument | string instrument, guitar, violin |
| food | food, apple, banana, berry, broccoli, carrot, citrus, coconut, egg, grape, pear, pumpkin, tomato, bread, cake, cheese, dessert, donut, fast food, hamburger, hot dog, ice cream, pizza, sandwich, sushi |
| drink | drink, hot drink, juice |
| dessert | dessert, cake, ice cream, donut |
| fast food | fast food, french fries, hot dog, pizza, hamburger, sandwich |
| furniture | furniture, bed, chair, couch, shelves, storage cabinet, table |
| jug | jug, teapot |
| lamp | lamp, candle |
| toy | toy, doll, teddy bear |
| flower | flower, rose, sunflower |
| animal | animal, bird, parrot, water bird, dolphin, fish, goldfish, jellyfish, seal, shellfish, whale, alpaca, bear, big cat, camel, cat, cow, crocodile, deer, dog, elephant, frog, giraffe, hippopotamus, horse, kangaroo, panda, pig, polar bear, rabbit, reptile, rhinoceros, sheep, squirrel, turtle, zebra |
| bird | bird, parrot, water bird |
| insect | insect, butterfly |
| fish | fish, goldfish |
| reptile | reptile, crocodile, frog, turtle |

</div>

</div>

## Person Detection Model Card v0.4<a href="#person-detection-model-card-v04" class="hash-link" aria-label="Direct link to Person Detection Model Card v0.4" title="Direct link to Person Detection Model Card v0.4">​</a>

### Model Details<a href="#model-details" class="hash-link" aria-label="Direct link to Model Details" title="Direct link to Model Details">​</a>

- Model last updated: 2024-02-29
- Model version: v0.4
- License: refer to the <a href="https://lightship.dev/terms/" target="_blank" rel="noopener noreferrer">terms of service</a> for Lightship.

### Technical specifications<a href="#technical-specifications" class="hash-link" aria-label="Direct link to Technical specifications" title="Direct link to Technical specifications">​</a>

The object detection model returns a set of bounding boxes and reports the probability that the box is a person, a human hand, or a human face.

### Intended use<a href="#intended-use" class="hash-link" aria-label="Direct link to Intended use" title="Direct link to Intended use">​</a>

#### Intended use cases<a href="#intended-use-cases" class="hash-link" aria-label="Direct link to Intended use cases" title="Direct link to Intended use cases">​</a>

- Identifying people (more specifically, human hands or human faces) in an image.
- Querying the presence or absence of people, human hands, or human faces in an image.

#### Permitted users<a href="#permitted-users" class="hash-link" aria-label="Direct link to Permitted users" title="Direct link to Permitted users">​</a>

Augmented reality developers through <a href="https://lightship.dev/" target="_blank" rel="noopener noreferrer">Niantic Lightship</a>.

#### Out-of-scope use cases<a href="#out-of-scope-use-cases" class="hash-link" aria-label="Direct link to Out-of-scope use cases" title="Direct link to Out-of-scope use cases">​</a>

This model does **not** provide the capability to:

- Track individuals
- Identify or recognise individuals

### Factors<a href="#factors" class="hash-link" aria-label="Direct link to Factors" title="Direct link to Factors">​</a>

The following factors apply to all object detection provided in the Lightship ARDK, including person detection:

- **Scale**: objects / classes may not be detected if they are very far away from the camera.
- **Lighting**: extreme light conditions may affect the overall performance.
- **Viewpoint**: extreme camera views that have not been seen during training may lead to a miss in detection or a class confusion.
- **Occlusion**: objects may not be detected if they are covered by other objects.
- **Motion blur**: fast camera or object motion may degrade the performance of the model.
- **Flicker**: there may be a ‘jittering’ effect between predictions of temporally adjacent frames.

For person detection specifically, based on known problems with computer vision technology, we identify potential relevant factors that include subgroups for:

- Geographical region
- Skin tone
- Gender
- Body posture: certain body configurations may be harder to predict due to appearing less often in the training corpus.
- Other: age, fashion style, accessories, body alterations, etc.

### Fairness evaluation<a href="#fairness-evaluation" class="hash-link" aria-label="Direct link to Fairness evaluation" title="Direct link to Fairness evaluation">​</a>

At Niantic, we strive for our technology to be inclusive and fair by following strict equality and fairness practices when building, evaluating, and deploying our models. We define person detection fairness as follows: a model makes fair predictions if it performs equally on images that depict a variety of the identified subgroups. The evaluation results focus on measuring the performance of the union of the human channels (person, human hand, and human face) on the first three main subgroups (geographical region, skin tone, and gender).

#### Instrumentation and dataset details<a href="#instrumentation-and-dataset-details" class="hash-link" aria-label="Direct link to Instrumentation and dataset details" title="Direct link to Instrumentation and dataset details">​</a>

Our benchmark dataset comprises 5650 images captured around the world using the back camera of a smartphone, with these specifications:

- Only one person per image is depicted.
- Both indoors and outdoors environments.
- Captured with a variety of devices.
- No occlusions.

Images are labeled with the following attributes:

- **Geographical region**: based on the <a href="https://en.wikipedia.org/wiki/Subregion" target="_blank" rel="noopener noreferrer">UN geoscheme</a> with the merge of European subregions and Micronesia, Polynesia, and Melanesia:
  - Northern Africa
  - Eastern Africa
  - Middle Africa
  - Southern Africa
  - Western Africa
  - Caribbean
  - Central America
  - South America
  - Northern America
  - Central Asia
  - Eastern Asia
  - South Eastern Asia
  - Southern Asia
  - Western Asia
  - Europe
  - Australia and New Zealand
  - Melanesia, Micronesia, and Polynesia
- **Skin tone**: following the <a href="https://en.wikipedia.org/wiki/Fitzpatrick_scale" target="_blank" rel="noopener noreferrer">Fitzpatrick scale</a>, images are annotated from subgroup 1 to 6. Skin tone is a self-reported value provided by the person in each image.
- **Gender**: images are annotated with self-reported gender.

#### Metrics<a href="#metrics" class="hash-link" aria-label="Direct link to Metrics" title="Direct link to Metrics">​</a>

The standard metric for evaluating object detection models -- and the one we use -- is <a href="https://towardsdatascience.com/intersection-over-union-iou-calculation-for-evaluating-an-image-segmentation-model-8b22e2e84686" target="_blank" rel="noopener noreferrer">Intersection over Union</a> (IoU). It is computed as follows:

IoU = (overlap between predicted and g.t. boxes) / (union between predicted and g.t. boxes)

Reported IoUs are averages (mean IoU or mIoU) over images belonging to the referenced subgroup unless stated otherwise.

#### Fairness criteria<a href="#fairness-criteria" class="hash-link" aria-label="Direct link to Fairness criteria" title="Direct link to Fairness criteria">​</a>

A model is considered to be making unfair predictions if it yields a performance (mIoU) for a particular subgroup that is three standard deviation units or more from the mean across all subgroups.

### Results<a href="#results" class="hash-link" aria-label="Direct link to Results" title="Direct link to Results">​</a>

#### Geographical evaluation<a href="#geographical-evaluation" class="hash-link" aria-label="Direct link to Geographical evaluation" title="Direct link to Geographical evaluation">​</a>

Average performance across all 17 regions is 78.74% with a standard deviation of 1.22%. All regions exhibit a performance in the range of \[76.92%, 82.17%\]. The maximum difference between the mean and the worst performing region is 1.83%, within our fairness criterion threshold of 3 standard deviations (3x1.22% = 3.65%).

| Regions                             | mIoU   | stdev  | Number of images |
|-------------------------------------|--------|--------|------------------|
| Northern Africa                     | 78.26% | 15.04% | 301              |
| Eastern Africa                      | 77.41% | 17.11% | 336              |
| Middle Africa                       | 77.30% | 15.72% | 322              |
| Southern Africa                     | 79.09% | 14.93% | 368              |
| Western Africa                      | 79.04% | 13.26% | 364              |
| Caribbean                           | 79.01% | 12.20% | 412              |
| Central America                     | 79.44% | 13.79% | 415              |
| South America                       | 78.39% | 14.21% | 397              |
| Northern America                    | 79.09% | 13.00% | 335              |
| Central Asia                        | 79.52% | 12.56% | 229              |
| Eastern Asia                        | 77.60% | 15.37% | 346              |
| South Eastern Asia                  | 77.86% | 14.86% | 333              |
| Southern Asia                       | 79.34% | 12.15% | 353              |
| Western Asia                        | 78.80% | 14.91% | 370              |
| Europe                              | 79.40% | 13.14% | 320              |
| Australia and New Zealand           | 76.92% | 18.13% | 374              |
| Melanesia, Micronesia and Polynesia | 82.17% | 11.08% | 75               |
| Average (across all images)         | 78.55% | 14.55% | 5650             |
| Average (across regions)            | 78.74% | 1.22%  | \-               |

#### Skin tone evaluation results<a href="#skin-tone-evaluation-results" class="hash-link" aria-label="Direct link to Skin tone evaluation results" title="Direct link to Skin tone evaluation results">​</a>

Average performance across all six skin tones is 78.58% with a standard deviation of 0.24%. All skin tone subgroups yield a performance in the range of \[78.23%, 78.97%\]. The maximum difference between the mean and the worst performing skin tone subgroup is 0.34%, within our fairness criterion threshold of 3 stdevs (3x0.24% = 0.71%).

| Skin tone (Fitzpatrick scale) | mIoU   | stdev  | Number of images |
|-------------------------------|--------|--------|------------------|
| 1                             | 78.59% | 12.00% | 247              |
| 2                             | 78.49% | 14.59% | 1919             |
| 3                             | 78.61% | 14.39% | 1463             |
| 4                             | 78.23% | 16.52% | 457              |
| 5                             | 78.97% | 13.60% | 706              |
| 6                             | 78.56% | 14.67% | 858              |
| Average (across all images)   | 78.55% | 14.55% | 5650             |
| Average (across skin tones)   | 78.58% | 0.24%  | \-               |

#### Gender evaluation results<a href="#gender-evaluation-results" class="hash-link" aria-label="Direct link to Gender evaluation results" title="Direct link to Gender evaluation results">​</a>

Average performance of all evaluated gender subgroups is 78.53% with a range \[78.01%, 79.05%\]. The difference between the average and the worst performing gender is 0.52%, within our fairness criterion threshold of 3 stdevs (3x0.74% = 2.22%).

| Perceived gender            | mIoU   | stdev  | Number of images |
|-----------------------------|--------|--------|------------------|
| Female                      | 78.01% | 15.08% | 2585             |
| Male                        | 79.05% | 13.96% | 3065             |
| Average (across all images) | 78.55% | 14.55% | 5650             |
| Average (across genders)    | 78.53% | 0.74%  | \-               |

### Ethical Considerations<a href="#ethical-considerations" class="hash-link" aria-label="Direct link to Ethical Considerations" title="Direct link to Ethical Considerations">​</a>

- **Privacy**: When the model is used in ARDK, inference is only applied on-device and the image is not transferred off the user device.
- **Human Life**: This model is designed for entertainment purposes within an augmented reality application. It is not intended to be used for making human life-critical decisions.
- **Bias**: Training datasets have not been audited for diversity and may present biases not surfaced by our benchmarks.

### Caveats and Recommendations<a href="#caveats-and-recommendations" class="hash-link" aria-label="Direct link to Caveats and Recommendations" title="Direct link to Caveats and Recommendations">​</a>

- Our annotated dataset only contains binary genders, which we include as male/female. Further data would be needed to evaluate across a spectrum of genders.
- An ideal skin tone evaluation dataset would additionally include camera details, and more environment details such as lighting and humidity. Furthermore, the Fitzpatrick scale has limitations as it doesn't fully represent the full spectrum of human skin tones.
- This model card is based on the work of Mitchell, Margaret, et al. "Model cards for model reporting." Proceedings of the conference on fairness, accountability, and transparency. 2019. <a href="https://arxiv.org/abs/1810.03993" target="_blank" rel="noopener noreferrer">Link</a>

</div>

</div>
