<?php

namespace backend\models;

use yii\base\Model;
use yii\data\ActiveDataProvider;
use backend\models\Subject;

/**
 * SubjectSearch represents the model behind the search form of `backend\models\Subject`.
 */
class SubjectSearch extends Subject
{
    /**
     * {@inheritdoc}
     */
    public function rules()
    {
        return [
            [['id', 'teach_id'], 'integer'],
            [['name', 'section', 'detail'], 'safe'],
        ];
    }

    /**
     * {@inheritdoc}
     */
    public function scenarios()
    {
        // bypass scenarios() implementation in the parent class
        return Model::scenarios();
    }

    /**
     * Creates data provider instance with search query applied
     *
     * @param array $params
     *
     * @return ActiveDataProvider
     */
    public function search($params)
    {
        $query = Subject::find();

        // add conditions that should always apply here

        $dataProvider = new ActiveDataProvider([
            'query' => $query,
        ]);

        $this->load($params);

        if (!$this->validate()) {
            // uncomment the following line if you do not want to return any records when validation fails
            // $query->where('0=1');
            return $dataProvider;
        }

        // grid filtering conditions
        $query->andFilterWhere([
            'id' => $this->id,
            'teach_id' => $this->teach_id,
        ]);

        $query->andFilterWhere(['like', 'name', $this->name])
            ->andFilterWhere(['like', 'section', $this->section])
            ->andFilterWhere(['like', 'detail', $this->detail]);

        return $dataProvider;
    }
}
