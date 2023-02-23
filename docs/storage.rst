Data Storage Primer
===================

The Old Way
-----------
For a long time, notebooks and pencils were the only methods to store data collected from scientific experiments. Although very useful and quick to set up, many limitations arise once datasets become larger and more complex. They are still used nowadays alongside computers during experimental research, but this is mostly for observations. Due to their fragility, they were set aside once computers emerged.

Magnetic Tapes
--------------
Magnetic tapes emerged in 1928 and are still used today as a reliable to store data that you don’t need to access regularly. This storage medium allows for data archiving, collection, and backup. They use Faraday’s induction law to create a mark specific to the input current.

.. image:: media/store.avif
   :width: 600

Tapes are harder to access than a hard drive as they need to be physically selected and read. On the other hand, this means that they are more secure than other storage mediums. The tape cannot be modified without being mounted in a drive. It also means that, if a drive fails, the data stored stays intact and safe. Compared to a hard drive, error rates for magnetic tapes are 4-5 orders of magnitude lower. Furthermore, they are energy efficient as they don’t use power when not in use. Because of these properties, scientists use magnetic tapes more for system backup, data archive and data exchange. Their low cost has kept them viable for long-term storage. CERN uses magnetic tapes for their archives. This allows them to store 4,2 exabytes [17 zeros!] of data. Included in this enormous number is not only scientific data – a lot of it comes from past and present high-energy physics experiments – but there are also photographs, videos, minutes, web pages, etc. It is truly an exercise in digital memory preservation.

It is safe to say that magnetic tapes will continue to be used for many more years. With new technological improvements (smaller magnetic particles, friction reduction…), they still have room to improve their capacity.

Hard Drives
-----------

Hard drives appeared in the 1950s. They are easy to use and access, and we can easily move around the different areas of the hard drive. Similarly to Magnetic tapes, they write in the data by magnetising thin layers of ferromagnetic materials. Because of the increased activity of their moving components, they last less time than magnetic tapes (around 3-5 years compared to the decades a tape has). The Event Horizon Telescope used 1,000 pounds of hard drives to store the 5 petabits [15 zeros!] of storage created by the observations leading to the first image of a black hole. In this case, due to the fragility of standard hard disks at high altitudes, researchers used helium drives. The internet would not have been capable of efficiently uploading all of the raw collected data. However, a cloud storage system was used to back up a reduced amount of data once analysed.

Distributed Data Storage
-------------------------

The increase in the use of open data created the need for a system in which users have access to a collection of distributed data storage from a single entry point. Data files are automatically cached locally, meaning users can have repeated access to the data without multiple downloads. Data is generated and passed on to users as and when they request it. Due to this, there is less of a limit on the amount of data stored. This method removes the complexity for the user as they do not need to know the internal structure of each data storage.

.. image:: media/store2.avif
   :width: 600

This system virtualises the storage facilities and allows scientists to bypass the construction of enormous centralised data storage. It is also easier and cheaper to scale up than physical data storage facilities. The capabilities of this virtual system remain the same with the possibility of having multiple forms of data stored within the design. A big downfall of this method would be the relative ease of access to the data. Compared to tapes, for example, there is a higher chance of accidental or intentional damage to the records. Although, the added use of blockchain technology would limit this considerably. For obvious reasons, this data storage method works well with research projects that have a strong international collaboration element to them. It has fostered large-scale scientific analysis. Facilities such as CERN and LIGO started using cloud storage several years ago. This allows them to create an open collaboration with scientists from all over the globe. As science becomes more and more data-heavy, virtual storage systems for scientific data analysis will only increase in future years.

References
-----------

* Kryukov, A. P., and A. P. Demichev. “Architecture of Distributed Data Storage for Astroparticle Physics.” Lobachevskii Journal of Mathematics, vol. 39, no. 9, 2018, pp. 1199–206, https://doi.org/10.1134/S1995080218090123.