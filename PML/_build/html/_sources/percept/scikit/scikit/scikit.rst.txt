Scikit-learn perceptron
=======================

Here we will try perceptron inside scikit-learn library

.. code:: ipython3

    import matplotlib.pyplot as plt
    
    import numpy as np
    from matplotlib import colors
    ll = ['#112031', '#152D35','#345B63', '#D4ECDD']
    ll.reverse()
    cmap = colors.ListedColormap(ll)
    
    from sklearn.datasets import load_digits
    from sklearn.linear_model import Perceptron
    X, y = load_digits(return_X_y=True)
    #what is random stat?
    clf = Perceptron(tol=1e-1, random_state=15, l1_ratio=0.25)
    clf.fit(X, y)





.. raw:: html

    <style>#sk-container-id-5 {color: black;background-color: white;}#sk-container-id-5 pre{padding: 0;}#sk-container-id-5 div.sk-toggleable {background-color: white;}#sk-container-id-5 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-5 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-5 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-5 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-5 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-5 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-5 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-5 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-5 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-5 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-5 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-5 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-5 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-5 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-5 div.sk-item {position: relative;z-index: 1;}#sk-container-id-5 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-5 div.sk-item::before, #sk-container-id-5 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-5 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-5 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-5 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-5 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-5 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-5 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-5 div.sk-label-container {text-align: center;}#sk-container-id-5 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-5 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-5" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>Perceptron(l1_ratio=0.25, random_state=15, tol=0.1)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-5" type="checkbox" checked><label for="sk-estimator-id-5" class="sk-toggleable__label sk-toggleable__label-arrow">Perceptron</label><div class="sk-toggleable__content"><pre>Perceptron(l1_ratio=0.25, random_state=15, tol=0.1)</pre></div></div></div></div></div>



let’s take a look to the first 18 data inside X dataset

.. code:: ipython3

    test = np.zeros((18,8,8))
    
    for i in range(18):
        test[i,:,:]=np.reshape(X[i],(8, 8))


.. code:: ipython3

    fig, axs = plt.subplots(3,6, figsize=(15, 6))
    
    axs = axs.ravel()
    
    
    for i in range(18):
        axs[i].imshow(test[i], cmap=cmap)



.. image:: output_4_0.png


lets see what predicted by our perceptron

.. code:: ipython3

    results= clf.predict(X)
    
    print("   prediction |  real value  |  difference")
    print("__________________________________________\n")
    
    for i in range(18):
        print("{:10d}    | {:10d}   |  {:10d}".format(results[i], y[i], results[i]-y[i]))


.. parsed-literal::

       prediction |  real value  |  difference
    __________________________________________
    
             0    |          0   |           0
             1    |          1   |           0
             2    |          2   |           0
             3    |          3   |           0
             4    |          4   |           0
             9    |          5   |           4
             6    |          6   |           0
             7    |          7   |           0
             8    |          8   |           0
             9    |          9   |           0
             0    |          0   |           0
             1    |          1   |           0
             2    |          2   |           0
             3    |          3   |           0
             4    |          4   |           0
             5    |          5   |           0
             6    |          6   |           0
             7    |          7   |           0


lets see how many results are accurate

.. code:: ipython3

    diff = results-y
    
    nonzeros = diff[diff!=0]
    
    nzlen=len(nonzeros)
    alldata=len(y)
    
    
    accuracy = (alldata-nzlen)/alldata
    
    print(accuracy)


.. parsed-literal::

    0.9710628825820813


Check output of perceprton score method

.. code:: ipython3

    clf.score(X,y)




.. parsed-literal::

    0.9710628825820813



Our estiamtion is very good !

