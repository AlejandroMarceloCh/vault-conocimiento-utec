---
curso: ACD
titulo: U3_L6 DataIntegration (parte 2)
slides: 0
fuente: U3_L6 DataIntegration (parte 2).ipynb
---

<div class="cell markdown" id="NDCNtQqKdX5C">

# **U3_L6 Data Integration**

## **Actividad:**

Analiza el notebook explicando lo que hace cada bloque de código agregando un bloque de comentario debajo de cada uno de los bloques.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:347,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718589102039,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="4onznKFa5HM_" outputId="8e947d87-8877-434c-943b-83c80127c724">

``` python
artist_df.info()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:241}" executionInfo="{&quot;elapsed&quot;:412,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718589124159,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="W7n4uMak5NDc" outputId="5d82abef-0fa0-48eb-b7a6-fa929c055f42">

``` python
artist_df.head()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:455}" executionInfo="{&quot;elapsed&quot;:388,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718589140205,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="B2tjViBNaDoW" outputId="b5b1b9af-eefc-46ce-8c2d-53860e1e6efe">

``` python
artist_df = artist_df.set_index('Artist').drop(columns=['X'])
artist_df
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:373,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718589145542,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="7_8QSHx40pPM" outputId="e98970fa-ab88-4fa5-d0f7-823bf2fa2c4c">

``` python
artist_df.loc['Drake']
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:382,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718589149312,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="UWZDtx0C0u-3" outputId="b2801988-5713-493a-c820-044b5df63d79">

``` python
artist_df.index.values
```

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:16673,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718589172281,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="33dt2aPl02KA">

``` python
for i,row in songIntegrate_df.iterrows():
    Artists = row.Artists.split(',')
    Artists = list(map(str.strip,Artists))
    ArtistsIn_artist_df = True
    for artist in Artists:
        if(artist not in artist_df.index.values):
            ArtistsIn_artist_df= False
            break
    if(not ArtistsIn_artist_df):
        continue

    songIntegrate_df.loc[i,'Artists_n_followers'] = 0
    songIntegrate_df.loc[i,'n_male_artists'] = 0
    songIntegrate_df.loc[i,'n_female_artists'] = 0
    songIntegrate_df.loc[i, 'artist_average_years_after_first_album'] = 0
    songIntegrate_df.loc[i, 'artist_average_number_albums'] = 0
    songIntegrate_df.loc[i,'n_bands'] = 0

    for artist in Artists:
        songIntegrate_df.loc[i,'Artists_n_followers'] += artist_df.loc[artist].Followers
        if(artist_df.loc[artist]['Group.Solo']=='Solo'):
            if(artist_df.loc[artist].Gender == 'M'):
                songIntegrate_df.loc[i,'n_male_artists'] += 1
            if(artist_df.loc[artist].Gender == 'F'):
                songIntegrate_df.loc[i,'n_female_artists'] += 1

        if(artist_df.loc[artist]['Group.Solo']=='Group'):
            if(artist_df.loc[artist].Gender == 'M'):
                songIntegrate_df.loc[i,'n_male_artists'] += 2
            if(artist_df.loc[artist].Gender == 'F'):
                songIntegrate_df.loc[i,'n_female_artists'] += 2
            songIntegrate_df.loc[i,'n_bands'] += 1
        First_date_on_Billboard = int(row.First_date_on_Billboard[:4])
        songIntegrate_df.loc[i, 'artist_average_years_after_first_album'] += \
            (First_date_on_Billboard - int(artist_df.loc[artist].YearFirstAlbum))

        songIntegrate_df.loc[i,
            'artist_average_number_albums'] += int(artist_df.loc[artist].NumAlbums)

    songIntegrate_df.loc[i,'artist_average_years_after_first_album'] /= len(Artists)
    songIntegrate_df.loc[i, 'artist_average_number_albums'] /= len(Artists)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:355,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718589213833,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="8racOmEm03W1" outputId="33cf34a2-e3b6-47d7-e66a-8c6d08057b48">

``` python
songIntegrate_df.info()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:669}" executionInfo="{&quot;elapsed&quot;:386,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718589220670,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="QEky3fpf5Yeg" outputId="c2ce9650-bd0a-4b20-8e59-4f664289e8a6">

``` python
songIntegrate_df
```

</div>
